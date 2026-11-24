# 重新編寫的示範，不是產品原碼
from fractions import Fraction


def compare_errors(baseline, candidate):
    """Compare mean error over exactly the same observations."""
    if not baseline or baseline.keys() != candidate.keys():
        raise ValueError("兩組必須含有相同且非空的觀測項目")
    count = len(baseline)
    before = Fraction(sum(baseline.values()), count)
    after = Fraction(sum(candidate.values()), count)
    return before, after, after - before


def main():
    baseline = {"甲": 8, "乙": 6, "丙": 4}
    candidate = {"甲": 6, "乙": 5, "丙": 4}
    before, after, change = compare_errors(baseline, candidate)
    print(f"基準平均誤差 {before}")
    print(f"候選平均誤差 {after}")
    print(f"候選減基準 {change}")


if __name__ == "__main__":
    main()
