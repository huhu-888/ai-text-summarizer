# AI 文本摘要助手

基于 DeepSeek 的文本摘要工具，支持 API 调用和网页界面。

## 功能

- 文本清洗
- 调用 DeepSeek 生成摘要
- FastAPI 接口 + 前端页面

## 技术栈

- Python 3.13
- FastAPI
- DeepSeek API
- HTML + JavaScript

## 快速开始

1. 安装依赖：
   pip install -r requirements.txt

2. 配置 Key：
   复制 day3/.env.example 为 day3/.env，填入你的 Key

3. 启动后端：
   cd day3
   uvicorn api:app --reload

4. 打开前端：
   浏览器打开 day3/frontend/index.html