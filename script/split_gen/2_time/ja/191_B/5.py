def main():
    #入力
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    #出力
    for i in range(N):
        if A[i] != X:
            print(A[i], end=" ")
