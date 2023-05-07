def main():
    N, M = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    # 金額が安い順にソート
    A, B = zip(*sorted(zip(A, B)))
    # 金額が安い順に買い集める
    ans = 0
    for i in range(N):
        if M <= B[i]:
            ans += M * A[i]
            break
        else:
            M -= B[i]
            ans += B[i] * A[i]
    print(ans)
