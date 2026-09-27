import json
from pathlib import Path

from cleaner import process
from llm_service import summarize

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.json"


def read_file(path: str) -> str:
    # Path 是类，Path(path) 是创建实例,path也就是其中的对象
    return Path(path).read_text(encoding="utf-8")


def save_json(data: dict, path: str) -> None:
    Path(path).write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def main():
    raw = read_file(INPUT_FILE)

    cleaned_list = process([raw])
    if not cleaned_list:
        print("文本为空，跳过")
        return

    text = cleaned_list[0]["content"]
    print(f"正文长度：{len(text)}")

    summary = summarize(text)
    print(f"摘要：{summary}")

    save_json({"text": text, "summary": summary}, OUTPUT_FILE)
    print(f"已保存到{OUTPUT_FILE}")


if __name__ == "__main__":
    main()
