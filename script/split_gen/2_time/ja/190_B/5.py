def main():
    #入力
    N, S, D = map(int, input().split())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    #処理
    for i in range(N):
        if X[i] < S and Y[i] > D:
            print("Yes")
            return
    print("No")
