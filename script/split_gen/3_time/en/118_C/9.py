def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 逆順に確認する
    A = A[::-1]
    # 1つ前のモンスターの体力が2倍以上になるように調整する
    for i in range(N - 1):
        if A[i] <= A[i + 1]:
            A[i + 1] = A[i] - 1
    # 体力が0未満になる場合は1にする
    for i in range(N):
        if A[i] < 1:
            A[i] = 1
    print(sum(A))
