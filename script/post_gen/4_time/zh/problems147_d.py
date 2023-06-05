Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(N):
            if (A[j] >> i) & 1:
                cnt += 1
        ans += (cnt * (N-cnt) * pow(2, i, mod)) % mod
        ans %= mod
    print(ans)

=======
Suggestion 2

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if a[j] & (1 << i):
                cnt += 1
        ans += cnt * (n - cnt) * (1 << i)
        ans %= (10 ** 9 + 7)
    print(ans)

=======
Suggestion 3

def xor_sum(n, a):
    ans = 0
    for i in range(n):
        ans ^= a[i]
    return ans

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int,input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if a[j] & (1<<i):
                cnt += 1
        ans += cnt*(n-cnt)*(1<<i)
        ans %= mod
    print(ans)

=======
Suggestion 5

def xor_sum(a):
    n = len(a)
    if n == 1:
        return 0
    else:
        return (a[0] ^ a[1]) + xor_sum(a[1:])

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(N):
            cnt += A[j]>>i&1
        ans += cnt*(N-cnt)*(1<<i)
        ans %= mod
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9+7
    ans = 0
    for i in range(60):
        zero = 0
        one = 0
        for j in range(N):
            if (A[j] >> i) & 1:
                one += 1
            else:
                zero += 1
        ans += ((1 << i) % MOD) * (one * zero)
        ans %= MOD
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 从二进制的最高位开始考虑，如果有两个数在最高位都是1，那么他们的XOR结果的最高位就是0，那么这个最高位的1就没有贡献了。
    # 因此，我们可以将所有数的最高位为1的数和最高位为0的数分开考虑，最后将两个部分的结果加起来即可。
    # 为了方便起见，我们先将所有数的二进制表示反转一下，这样最高位为1的数就变成了最低位为1的数，这样就可以从最低位开始考虑了。
    # 考虑最低位，如果有两个数最低位都是1，那么他们的XOR结果的最低位就是0，那么这个最低位的1就没有贡献了。
    # 因此，我们可以将所有数的最低位为1的数和最低位为0的数分开考虑，最后将两个部分的结果加起来即可。
    # 为了方便起见，我们先将所有数的二进制表示反转一下，这样最低位为1的数就变成了最高位为1的数，这样就可以从最高位开始考虑了。
    # 重复上述过程，就可以得到最终的答案了。
    # 为了更好的理解这个过程，可以看看下面的例子：
    # 3 1 4 1 5 9 2 6 5 3
    # 3 1 4 1 5 9 2 6 5 3
    # 1 3 1 4 1 5 9 2 6 5
    # 1 3 1 4 1 5

=======
Suggestion 9

def XOR(a,b):
    if a == b:
        return 0
    else:
        return 1

=======
Suggestion 10

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    # 1. 2^k位上有1的数字
    # 2. 2^k位上有0的数字
    # 3. 2^k位上有1的数字的个数
    # 4. 2^k位上有0的数字的个数
    # 5. 2^k位上有1的数字的总和
    # 6. 2^k位上有0的数字的总和
    # 7. 2^k位上有1的数字的总和的模数（10^9+7）
    # 8. 2^k位上有0的数字的总和的模数（10^9+7）
    # 9. 2^k位上有1的数字的个数的模数（10^9+7）
    # 10. 2^k位上有0的数字的个数的模数（10^9+7）
    # 11. 2^k位上有1的数字的个数的模数（10^9+7）
    # 12. 2^k位上有0的数字的个数的模数（10^9+7）

    # 1. 2^k位上有1的数字
    # 2. 2^k位上有0的数字
    # 3. 2^k位上有1的数字的个数
    # 4. 2^k位上有0的数字的个数
    # 5. 2^k位上有1的数字的总和
    # 6. 2^k位上有0的数字的总和
    # 7. 2^k位上有1的数字的总和的模数（10^9+7）
    # 8. 2^k位上有0的数字的总和的模数（10^9+7）
    # 9. 2^k位上有1的数字的个数的模数（10^9+7）
    # 10. 2^k位上有0
