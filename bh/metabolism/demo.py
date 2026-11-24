# 重新編寫的示範，不是產品原碼
import json


def duplicate_groups(samples):
    """Compare exact contents within each declared sample category."""
    by_category = {}
    for label, category, content in samples:
        by_content = by_category.setdefault(category, {})
        by_content.setdefault(content, []).append(label)

    return {
        category: [labels for labels in by_content.values() if len(labels) > 1]
        for category, by_content in by_category.items()
    }


if __name__ == "__main__":
    samples = [
        ("甲", "圖樣", b"circle"),
        ("乙", "圖樣", b"circle"),
        ("丙", "文字", b"note"),
        ("丁", "文字", b"caption"),
        ("戊", "文字", b"circle"),
    ]
    print(json.dumps(duplicate_groups(samples), ensure_ascii=False))
    print("輸入保留筆數", len(samples))
