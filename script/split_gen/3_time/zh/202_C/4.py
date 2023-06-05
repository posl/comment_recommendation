def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    #Cの要素の値-1をインデックスとして、Bの要素の値を格納する配列
    D = [0] * N
    for i in range(N):
        D[C[i] - 1] += 1
    #Aの要素の値-1をインデックスとして、Dの要素の値を格納する配列
    E = [0] * N
    for i in range(N):
        E[A[i] - 1] += D[i]
    ans = 0
    for i in range(N):
        ans += E[B[i] - 1]
    print(ans)
