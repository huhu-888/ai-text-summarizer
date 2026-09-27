#从cleaner模块里导入process函数
from cleaner import process


def main():
    raw_texts = [
        "  今天天气不错  ",
        "",
        "   ",
        "Python 是一门好语言",
        "AI 正在改变世界",
        "\n\t  ",
        "学习要循序渐进",
        "今天 任务 完成"
    ]

    results = process(raw_texts)

    print("+" * 40)
    print("清洗结果：")
    print("+" * 40)
    for item in results:
        print(f"正文：{item['content']}")
        print(f"字符数：{item['length']}")
        print("+" * 40)

    print(f"共处理{len(results)}条有效文本")


if __name__ == "__main__":
    main()