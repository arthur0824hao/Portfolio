# 重新編寫的示範，不是產品原碼
from hashlib import sha256


def fingerprint(body):
    return sha256(body.encode("utf-8")).hexdigest()


def reconcile(messages, receipts):
    """Match each fictional message to a receipt for the same revision."""
    observed = {}
    for message_id, digest in receipts:
        observed.setdefault(message_id, set()).add(digest)

    states = {}
    for message_id, body in messages.items():
        versions = observed.get(message_id, set())
        if fingerprint(body) in versions:
            states[message_id] = "相符"
        elif versions:
            states[message_id] = "版本不符"
        else:
            states[message_id] = "缺回條"
    return states


def main():
    messages = {"甲": "初稿", "乙": "二稿", "丙": "結語"}
    receipts = [
        ("甲", fingerprint("初稿")),
        ("甲", fingerprint("初稿")),
        ("乙", fingerprint("一稿")),
    ]
    for message_id, state in reconcile(messages, receipts).items():
        print(f"{message_id} → {state}")


if __name__ == "__main__":
    main()
