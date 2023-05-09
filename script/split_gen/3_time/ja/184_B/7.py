def main():
    #入力
    N, X = map(int, input().split())
    S = input()
    #処理
    for i in range(N):
        if S[i] == "o":
            X += 1
        else:
            if X > 0:
                X -= 1
    #出力
    print(X)
