def solve():
    N, C = map(int, input().split())
    #print(N, C)
    abc = []
    for i in range(N):
        a, b, c = map(int, input().split())
        #print(a, b, c)
        abc.append((a, b, c))
    #print(abc)
    # 1日ごとに支払う金額を計算する
    day = [0] * (10 ** 9 + 2)
    for a, b, c in abc:
        day[a] += c
        day[b + 1] -= c
    #print(day)
    # 累積和を計算する
    for i in range(1, len(day)):
        day[i] += day[i - 1]
    #print(day)
    # すぬけプライムに加入する日を探す
    prime = [0] * (10 ** 9 + 2)
    for i in range(1, len(day)):
        if day[i] > C:
            prime[i] = 1
    #print(prime)
    # 累積和を計算する
    for i in range(1, len(prime)):
        prime[i] += prime[i - 1]
    #print(prime)
    # 各サービスを利用する日を探す
    ans = 0
    for a, b, c in abc:
        if prime[b] - prime[a - 1] == 0:
            ans += c
    print(ans)

if __name__ == '__main__':
    solve()