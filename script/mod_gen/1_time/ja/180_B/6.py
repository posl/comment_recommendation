def main():
    N = int(input())
    X = list(map(int, input().split()))
    #print("N =", N)
    #print("X =", X)
    # マンハッタン距離
    sum = 0
    for i in range(N):
        sum += abs(X[i])
    print(sum)
    # ユークリッド距離
    sum = 0
    for i in range(N):
        sum += X[i] * X[i]
    print(sum ** 0.5)
    # チェビシェフ距離
    max = 0
    for i in range(N):
        if max < abs(X[i]):
            max = abs(X[i])
    print(max)

if __name__ == '__main__':
    main()