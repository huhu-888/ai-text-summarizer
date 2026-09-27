import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("DEEPSEEK_API_KEY")
BASE_URL = os.getenv("DEEPSEEK_BASE_URL")

if not API_KEY:
    raise RuntimeError("缺少DEEPSEEK_API_KEY，请配置")

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)


def summarize(text: str) -> str:
    """输入正文返回摘要"""
    # 空文本不调用模型,当以下为真，空文本为假，直接返回空
    if not text or not text.strip():
        return ""

    try:
        response = client.chat.completions.create(
            model="deepseek-flash",
            messages=[
                {"role": "system", "content": "你是一个翻译助手，把用户输入翻译成英文。"},
                {"role": "user", "content": text},
            ],
            temperature=0.3,
        )
        summary = response.choices[0].message.content
        if not summary:
            raise RuntimeError("模型返回为空")
        return summary.strip()
    except Exception as e:
        raise RuntimeError(f"模型调用失败：{e}")
