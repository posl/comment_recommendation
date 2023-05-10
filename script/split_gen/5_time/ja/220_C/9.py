def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    # Aの合計値
    sum_A = sum(A)
    # Aの最大値
    max_A = max(A)
    # Aの最小値
    min_A = min(A)
    # Aの合計値の桁数
    digit_sum_A = len(str(sum_A))
    # XがAの合計値以下の場合は、XをAの合計値の桁数分繰り返した数列Bの項を前から順に足したとき、和が初めてXを超えるのは何項目まで足したときかを求める
    if X <= sum_A:
        # XをAの合計値の桁数分繰り返した数列B
        B = str(X) * digit_sum_A
        # Bの項を前から順に足したとき、和が初めてXを超えるのは何項目まで足したときかを求める
        for i in range(1, digit_sum_A + 1):
            if X < int(B[:i]):
                print(i - 1)
                exit()
    # XがAの合計値より大きい場合は、XをAの最大値の桁数分繰り返した数列Bの項を前から順に足したとき、和が初めてXを超えるのは何項目まで足したときかを求める
    else:
        # XをAの最大値の桁数分繰り返した数列B
        B = str(X) * len(str(max_A))
        # Bの項を前から順に足したとき、和が初めてXを超えるのは何項目まで足したときかを求める
        for i in range(1, len(str(max_A)) + 1):
            if X < int
