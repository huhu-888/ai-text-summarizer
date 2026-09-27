# AI 文本摘要助手

基于 DeepSeek 的文本摘要工具，支持 API 调用和网页界面。

## 功能

- 文本清洗（去首尾空白、过滤空内容）
- 调用 DeepSeek 生成摘要
- FastAPI 接口，支持 API 调用
- 简单前端页面

## 技术栈

- Python 3.13
- FastAPI + uvicorn
- DeepSeek API（通过 openai 库调用）
- python-dotenv 管理环境变量
- HTML + JavaScript

## 目录结构

```
ai-text-summarizer/
├── day1/                    # 文本清洗脚本
│   ├── cleaner.py           # 清洗函数
│   └── main.py              # 入口
├── day2/                    # 模型调用
│   ├── cleaner.py
│   ├── llm_service.py       # 封装 summarize 函数
│   ├── input.txt            # 测试文本
│   └── main.py              # 读文件 → 清洗 → 摘要 → 存 JSON
└── day3/                    # FastAPI 接口 + 前端
    ├── cleaner.py
    ├── llm_service.py
    ├── api.py               # FastAPI 接口
    └── frontend/
        └── index.html       # 前端页面
```

## 依赖安装

```bash
pip install -r requirements.txt
```

## 环境变量

1. 复制示例文件：

```bash
cp day3/.env.example day3/.env
```

2. 编辑 `day3/.env`，填入你的 DeepSeek API Key：

```
DEEPSEEK_API_KEY=sk-你的Key
DEEPSEEK_BASE_URL=https://api.deepseek.com
```

> API Key 获取：https://platform.deepseek.com

## 启动方式

### 后端

```bash
cd day3
uvicorn api:app --reload
```

启动后：

- 接口地址：http://127.0.0.1:8000/summarize
- 文档页面：http://127.0.0.1:8000/docs

### 前端

浏览器打开 `day3/frontend/index.html`。

## 请求示例

### curl

```bash
curl -X POST http://127.0.0.1:8000/summarize \
  -H "Content-Type: application/json" \
  -d '{"text": "Python 是一门广泛使用的编程语言。"}'
```

### 请求体

```json
{
  "text": "待摘要的正文",
  "max_length": 20
}
```

### 响应

```json
{
  "summary": "生成的摘要"
}
```

## 错误状态码

| 状态码 | 含义 | 原因 |
|--------|------|------|
| 200 | 成功 | 正常返回摘要 |
| 400 | 请求错误 | 空文本、超长 |
| 401 | 未认证 | API Key 错误 |
| 402 | 需要付费 | 余额不足 |
| 422 | 校验失败 | 缺字段、类型错 |
| 500 | 服务器错误 | 模型调用失败 |
