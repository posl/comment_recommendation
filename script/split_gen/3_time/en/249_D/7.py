def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A_iの約数を列挙する
    divisors = [[] for _ in range(2 * 10**5 + 1)]
    for i in range(1, 2 * 10**5 + 1):
        for j in range(i, 2 * 10**5 + 1, i):
            divisors[j].append(i)
    # A_iの約数のうち、A_jの約数の数を数える
    cnt = [0] * (2 * 10**5 + 1)
    for a in A:
        for d in divisors[a]:
            cnt[d] += 1
    # A_iの約数のうち、A_jの約数の数が2以上のものを列挙する
    # これらの数は、A_kの約数でもある
    # このとき、A_iの約数のうち、A_jの約数の数が2以上のものの個数を数える
    ans = 0
    for a in A:
        for d in divisors[a]:
            if cnt[d] >= 2:
                ans += 1
                break
    print(ans)
