def clean_text(text: str) -> str:
    if not isinstance(text,str):
        return ""    
    return text.strip()


def filter_empty(texts: list[str]) -> list[str]:
    result = []
    for t in texts:
        cleaned=clean_text(t)
        if cleaned:
            result.append(cleaned)
    return result

def build_result(texts: list[str]) -> list[dict]:
    result=[]
    for t in texts:
        result.append({"content":t ,
                       "length":len(t),
                    })
    return result


def process(texts: list[str]) -> list[dict]:
    cleaned = [clean_text(t) for t in texts]
    filtered=filter_empty(cleaned)
    return build_result(filtered)

