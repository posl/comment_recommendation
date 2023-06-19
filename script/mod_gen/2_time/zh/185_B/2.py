def solve():
    N, M, T = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 1.5, 2.5, ...の時間が充電可能な時間
    chargeable = []
    for i in range(M):
        chargeable.append(A[i] - B[i] - 1)
    chargeable.append(T - B[M - 1] - 1)
    # 充電可能な時間の合計
    chargeable_sum = 0
    for i in range(M + 1):
        chargeable_sum += chargeable[i]
    # 充電可能な時間の合計がNを超えなければYes
    if chargeable_sum * 2 >= N:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()