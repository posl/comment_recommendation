Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(40, -1, -1):
        cnt = 0
        for a in A:
            if a & (1 << i):
                cnt += 1
        if cnt * 2 < N:
            ans += 1 << i
        if ans + (1 << i) - 1 <= K:
            ans += 1 << i
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(40, -1, -1):
        if k & (1 << i):
            cnt = 0
            for j in range(n):
                if a[j] & (1 << i):
                    cnt += 1
            if cnt * 2 < n:
                ans += 1 << i
            k -= 1 << i
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(40, -1, -1):
        zero = 0
        one = 0
        for a in A:
            if a >> i & 1:
                one += 1
            else:
                zero += 1
        if K >> i & 1:
            ans += (1 << i) * one
            A = [a for a in A if a >> i & 1]
        else:
            ans += (1 << i) * zero
            A = [a for a in A if not a >> i & 1]
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    X = 0
    for i in range(50, -1, -1):
        if X + (1 << i) <= K:
            X += (1 << i)
            if (N - 1) % 2 == 0:
                if A[0] & (1 << i) == 0:
                    A = [a ^ X for a in A]
                    A.sort()
    ans = 0
    for a in A:
        ans += a ^ X
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # Kの2進数表記を求める
    k_bin = bin(K)[2:]
    # 2進数表記の桁数を求める
    k_len = len(k_bin)
    # 2進数表記の桁数のうち、0の桁数を求める
    zero_num = k_bin.count('0')
    # 2進数表記の桁数のうち、1の桁数を求める
    one_num = k_len - zero_num
    # 2進数表記の桁数のうち、1の桁数を求める
    one_num = k_len - zero_num
    # 2進数表記の桁数のうち、0の桁数を求める
    zero_num = k_bin.count('0')
    # Kの2進数表記を求める
    k_bin = bin(K)[2:]
    # 2進数表記の桁数を求める
    k_len = len(k_bin)
    # 2進数表記の桁数のう

=======
Suggestion 6

def solve(n, k, a):
    # a XOR b = c
    # a XOR c = b
    # b XOR c = a
    # a + b + c = 0
    # a + b = -c
    # a = -c - b

    # 0 <= a <= k
    # 0 <= k <= 10 ** 12
    # 0 <= a <= 10 ** 12

    # a + b = -c
    # a + b = -c
    # a + b = -a - b
    # 2 * a + b = 0
    # b = -2 * a

    # 0 <= b <= k
    # 0 <= -2 * a <= k
    # 0 <= -a <= k / 2
    # 0 <= a <= k / 2

    # a + b = -c
    # a + b = -a - b
    # b = -c - a
    # b = -a - a
    # b = -2 * a

    # 0 <= b <= k
    # 0 <= -2 * a <= k
    # 0 <= -a <= k / 2
    # 0 <= a <= k / 2

    # a + b = -c
    # a + b = -a - b
    # a = -c - b
    # a = -b - b
    # a = -2 * b

    # 0 <= a <= k
    # 0 <= -2 * b <= k
    # 0 <= -b <= k / 2
    # 0 <= b <= k / 2

    # a + b = -c
    # a + b = -a - b
    # a = -c - b
    # b = -c - a
    # a = -b - b
    # b = -a - a
    # a = -2 * b
    # b = -2 * a

    # 0 <= a <= k
    # 0 <= -2 * b <= k
    # 0 <= -b <= k / 2
    # 0 <= b <= k / 2

    # a

=======
Suggestion 7

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(N, K, A)

    def check(X):
        #print(X)
        a = 0
        for i in range(N):
            #print(a, A[i], X)
            a += (A[i] ^ X)
        #print(a)
        return a <= K

    #print(check(2))

    X = 0
    for i in range(40, -1, -1):
        if (X + (1 << i)) <= A[-1] and check(X + (1 << i)):
            X += (1 << i)
        #print(X)
    print(X + K)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    print(A)
    #print(A[0], A[1])
    #print(A[0] ^ A[1])
    #print(A[0] ^ A[1] ^ A[2])
    #print(A[0] ^ A[1] ^ A[2] ^ A[3])
    print(A[0] ^ A[1] ^ A[2] ^ A[3])

=======
Suggestion 9

def solve(N,K,A):
    # print(N,K,A)
    ans = 0
    for i in range(60,-1,-1):
        if K & (1 << i) == 0:
            continue
        else:
            if ans + (1 << i) > K:
                continue
            else:
                ans += (1 << i)
    # print(ans)
    cnt = [0] * 61
    for i in range(N):
        for j in range(60,-1,-1):
            if A[i] & (1 << j) == 0:
                continue
            else:
                cnt[j] += 1
    # print(cnt)
    ans2 = 0
    for i in range(60,-1,-1):
        if ans & (1 << i) == 0:
            ans2 += (1 << i) * cnt[i]
        else:
            ans2 += (1 << i) * (N - cnt[i])
    print(ans2)

=======
Suggestion 10

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, A)

    # Kの各bitについて、Aのbitが立っている数を数える
    # 1. そのbitが立っている数がN/2より大きい場合、そのbitは0になる
    # 2. そのbitが立っている数がN/2より小さい場合、そのbitは1になる
    # 3. そのbitが立っている数がN/2の場合、そのbitはKのbitによって決まる
    # 3-1. Kのbitが0の場合、そのbitは0になる
    # 3-2. Kのbitが1の場合、そのbitは1になる
    # 3-3. Kのbitが0の場合、そのbitは1になる

    # 1. 2. については、bitが立っている数を数えるだけで良い
    # 3. については、bitが立っている数がN/2の場合、そのbitはKのbitによって決まる
    # 3-1. 3-2. については、bitが立っている数を数えるだけで良い
    # 3-3. については、bitが立っている数がN/2の場合、そのbitは1になる

    # bitが立っている数を数える
    bit_count = [0] * 64
    for a in A:
        for i in range(64):
            if a & (1 << i):
                bit_count[i] += 1

    # bitが立っている数がN/2より大きい場合、そのbitは0になる
    # bitが立っている数がN/2より小さい場合、そのbitは1になる
    # bit
