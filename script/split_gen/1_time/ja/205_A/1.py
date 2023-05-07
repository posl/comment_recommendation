def main():
    A, B = map(int, input().split())
    # 100 mL あたり A kcal のエネルギーを持つドリンクがあります。このドリンク B mL は何 kcal のエネルギーを持つでしょうか？
    print(A * B / 100)
