def clean_text(text: str) -> str:
    """去掉首尾空白"""
    if not isinstance(text, str):
        return ""
    return text.strip()


def filter_empty(texts: list[str]) -> list[str]:
    """过滤整条空内容"""
    result = []
    for t in texts:
        cleaned=clean_text(t)
        if cleaned:
            result.append(cleaned)
    return result


def build_result(texts: list[str]) -> list[dict]:
    """构建结果列表"""
    result = []
    for t in texts:
        result.append({
            "content": t,
            "length": len(t),
        })
    return result




def process(texts: list[str]) -> list[dict]:
    """
    完整流程：清洗 -> 过滤 -> 构建结果
    """
    cleaned = [clean_text(t) for t in texts]
    filtered = filter_empty(cleaned)
    return build_result(filtered)

