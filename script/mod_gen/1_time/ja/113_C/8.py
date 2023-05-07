def main():
    N, M = map(int, input().split())
    #市の誕生年のリスト
    Y = []
    #県の市の数のリスト
    P = [0] * N
    for _ in range(M):
        p, y = map(int, input().split())
        Y.append([p, y])
        P[p - 1] += 1
    #県の市の数の累積和リスト
    P = [0] + list(accumulate(P))
    #市の認識番号のリスト
    ans = []
    for p, y in Y:
        ans.append(str(p).zfill(6) + str(P[p - 1]).zfill(6))
        P[p - 1] += 1
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()