def main():
    #入力
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        A_i, B_i = map(int, input().split())
        A.append(A_i)
        B.append(B_i)
    #問題の解答
    ans = 3**N
    for i in range(M):
        if A[i] == B[i]:
            ans -= 3**(N - 1)
    #出力
    print(ans)
