# 重新編寫的示範，不是產品原碼
from graphlib import TopologicalSorter


def ready_tasks(dependencies, completed):
    """List unfinished tasks whose prerequisites are all complete."""
    known = set(dependencies)
    required = {item for items in dependencies.values() for item in items}
    if (required | completed) - known:
        raise ValueError("清單中有未定義的工作")
    # Reject cycles, even if an unrelated task is ready.
    tuple(TopologicalSorter(dependencies).static_order())
    if any(not dependencies[name] <= completed for name in completed):
        raise ValueError("完成清單缺少必要的前置工作")
    return [name for name, needs in dependencies.items()
            if name not in completed and needs <= completed]


def main():
    tasks = {
        "整理": set(),
        "核算": {"整理"},
        "校字": {"整理"},
        "交稿": {"核算", "校字"},
    }
    snapshots = [
        ("起點", set()),
        ("完成整理", {"整理"}),
        ("再完成核算", {"整理", "核算"}),
        ("再完成校字", {"整理", "核算", "校字"}),
    ]
    for label, completed in snapshots:
        print(f"{label} → {'、'.join(ready_tasks(tasks, completed))}")


if __name__ == "__main__":
    main()
