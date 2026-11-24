# 重新編寫的示範，不是產品原碼
import json


def layers(prerequisites):
    """Group invented components by the earliest layer they can enter."""
    names = set(prerequisites)
    unknown = {p for needed in prerequisites.values() for p in needed} - names
    if unknown:
        raise ValueError("找不到前置元件")

    completed = set()
    result = []
    while len(completed) < len(names):
        ready = [
            name for name, needed in prerequisites.items()
            if name not in completed and all(p in completed for p in needed)
        ]
        if not ready:
            raise ValueError("相依成環")
        result.append(ready)
        completed.update(ready)
    return result


if __name__ == "__main__":
    poster = {"底稿": [], "圖形": ["底稿"], "文字": ["底稿"], "樣張": ["圖形", "文字"]}
    print(json.dumps(layers(poster), ensure_ascii=False))
    try:
        layers({"甲": ["乙"], "乙": ["甲"]})
    except ValueError as error:
        print(str(error))
