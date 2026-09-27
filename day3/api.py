"""
FastAPI 接口
运行：uvicorn api:app --reload
调试：http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware 

from llm_service import summarize

# 创建应用
app = FastAPI(title="AI 文本摘要助手")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # 允许所有来源（开发用，生产要收紧）
    allow_methods=["*"],
    allow_headers=["*"],
)

# 请求体模型 text字段
class SummarizeRequest(BaseModel):
    text: str = Field(..., description="待摘要的正文")

#响应体模型 summary字段
class SummarizeResponse(BaseModel):
    summary: str


MAX_LENGTH = 500

#声明 POST 接口
@app.post("/summarize", response_model=SummarizeResponse)
def do_summarize(req: SummarizeRequest):
    #收到SummarizeRequest的text值

    #返回状态码，API里用状态码表达结果400就是错误，所以用raise
    if not req.text or not req.text.strip():
        raise HTTPException(status_code=400, detail="文本不能为空")

    if len(req.text) > MAX_LENGTH:
        raise HTTPException(
            status_code=400,
            detail=f"文本过长，最多 {MAX_LENGTH} 字符",
        )

    try:
        #调用summarize函数
        summary = summarize(req.text)
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))

    #结果存在summary里了，给定义的字段赋值
    return SummarizeResponse(summary=summary)
