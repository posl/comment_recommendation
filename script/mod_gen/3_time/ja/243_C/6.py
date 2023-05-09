def main():
    #入力
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    S = input()
    #処理
    count = 0
    for i in range(N):
        if S[i] == "R":
            for j in range(i+1, N):
                if S[j] == "L":
                    if X[i] < X[j]:
                        if Y[i] == Y[j]:
                            count += 1
    #出力
    if count >= 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()