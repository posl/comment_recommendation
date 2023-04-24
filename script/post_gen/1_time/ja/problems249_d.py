Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if A[i] * A[j] == A[k]:
                    count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans += (a[i] * a[j]) // a[i]
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(0, N):
        for j in range(i, N):
            for k in range(j, N):
                if (A[i] / A[j]) == A[k]:
                    ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    #print(A)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += A.count(A[i] * A[j])
    print(ans)

=======
Suggestion 6

def solve(n, a):
    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and k != i and a[i] / a[j] == a[k]:
                    ans += 1
    return ans

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    dp = [0] * (A[-1]+1)
    for i in range(N):
        dp[A[i]] += 1
    ans = 0
    for i in range(1, A[-1]+1):
        cnt = 0
        for j in range(i, A[-1]+1, i):
            cnt += dp[j]
        if cnt >= 2:
            ans += cnt * (cnt-1) // 2
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    count = [0] * (A[-1]+1)
    for i in A:
        count[i] += 1
    ans = 0
    for i in A:
        if i == 0:
            continue
        for j in A:
            if i > j:
                continue
            if i == j:
                ans += (count[i] * (count[i]-1)) // 2
                break
            if (i * j) % (i - j) == 0:
                k = (i * j) // (i - j)
                if k in A:
                    ans += count[i] * count[j]
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # Aの最大値を求める
    max_A = max(A)

    # Aの最大値の約数を求める
    # 約数を格納するリスト
    divisors = []
    # 約数の数を格納するリスト
    num_divisors = []
    # 約数の数の合計を格納するリスト
    sum_divisors = []

    # 1からmax_Aまでの数について
    for i in range(1, max_A + 1):
        # 約数を格納するリスト
        divisors.append([])
        # 約数の数を格納するリスト
        num_divisors.append(0)
        # 約数の数の合計を格納するリスト
        sum_divisors.append(0)

        # 1からiまでの数について
        for j in range(1, i + 1):
            # iをjで割り切れるなら
            if i % j == 0:
                # 約数を格納するリストにjを追加
                divisors[i].append(j)
                # 約数の数を格納するリストに1を追加
                num_divisors[i] += 1

    # 約数の数の合計を格納するリストを求める
    for i in range(1, max_A + 1):
        # 1からiまでの数について
        for j in range(1, i + 1):
            # 約数の数の合計を格納するリストにiの約数の数を追加
            sum_divisors[i] += num_divisors[j]

    # 約数の数の合計を格納するリストを求める
    for i in range(1, max_A + 1):
        # 1からiま

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)

    #Aの中の最大値を探す
    max_A = 0
    for i in range(N):
        if max_A < A[i]:
            max_A = A[i]

    #Aの中にある数値の個数をカウントする
    cnt_A = [0] * (max_A + 1)
    for i in range(N):
        cnt_A[A[i]] += 1

    #Aの中の数値の個数を累積和にする
    for i in range(max_A):
        cnt_A[i+1] += cnt_A[i]

    #Aの中にある数値の個数を累積和にする
    cnt_A = [0] + cnt_A

    #Aの中にある数値の個数を累積和にする
    cnt_A = [0] + cnt_A

    #Aの中にある数値の個数を累積和にする
    cnt_A = [0] + cnt_A

    #Aの中の数値の個数を累積和にする
    for i in range(max_A):
        cnt_A[i+1] += cnt_A[i]

    #Aの中にある数値の個数を累積和にする
    cnt_A = [0] + cnt_A

    #Aの中にある数値の個数を累積和にする
    cnt_A = [0] + cnt_A

    #Aの中にある数値の個数を累積和にする
    cnt_A = [0] + cnt_A

    #Aの中の数値の個数を累積和にする
    for i in range(max_A):
        cnt_A[i+1] += cnt_A[i]

    #Aの中にある数値の個数を累積和にする
    cnt_A = [0] + cnt_A

    #Aの中にあ
