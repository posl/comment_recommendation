def main():
    N, M = map(int, input().split())
    MOD = 10 ** 9 + 7
    # Mの約数を列挙
    divisors = []
    i = 1
    while i * i <= M:
        if M % i == 0:
            divisors.append(i)
            if i * i != M:
                divisors.append(M // i)
        i += 1
    divisors.sort()
    # 約数の数を数える
    cnt = [0] * len(divisors)
    for i in range(len(divisors)):
        cnt[i] = pow(M // divisors[i], N, MOD)
        for j in range(i):
            if divisors[i] % divisors[j] == 0:
                cnt[i] -= cnt[j]
                cnt[i] %= MOD
    # 約数の数の和を求める
    ans = 0
    for i in range(len(divisors)):
        ans += cnt[i] * divisors[i]
        ans %= MOD
    print(ans)
