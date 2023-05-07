def main():
    #入力
    N = int(input())
    S = list(map(int, input().split()))
    #Aの初期値
    A = [0 for i in range(N)]
    #Aの最初の要素を決める
    A[0] = S[0]
    #Aの残りの要素を決める
    for i in range(1, N):
        A[i] = S[i] - A[i-1]
    #出力
    print(*A)
