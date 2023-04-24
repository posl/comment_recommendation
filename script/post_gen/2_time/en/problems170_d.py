Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(1, N):
        if A[i] != A[i - 1]:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-1):
        if A[i] == A[i+1]:
            continue
        if A[i+1] % A[i] != 0:
            ans += 1
    print(ans + 1)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if i == 0:
            if A[0] != A[1]:
                ans += 1
        elif i == N - 1:
            if A[N - 1] != A[N - 2]:
                ans += 1
        else:
            if A[i] != A[i - 1] and A[i] != A[i + 1]:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    ans = 0
    for i in range(1, N):
        if A[i] != A[i-1]:
            ans += 1
    print(ans+1)

=======
Suggestion 6

def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    ans = 0
    for i in range(N):
        if A[i] != A[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    ans = 0
    for i in range(n):
        if i == 0:
            ans += 1
        elif a[i] != a[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # A_i が素数かどうかを格納するリスト
    is_prime = [True] * (10**6 + 1)

    # A_i が素数かどうかを判定する
    for i in range(2, (10**6 + 1)):
        if is_prime[i]:
            for j in range(i * 2, (10**6 + 1), i):
                is_prime[j] = False

    # A_i が素数の場合のみ、A_i で割り切れる数を除外する
    for i in range(N):
        if is_prime[A[i]]:
            for j in range(A[i], (10**6 + 1), A[i]):
                is_prime[j] = False

    # A_i が素数の数をカウントする
    count = 0
    for i in range(N):
        if is_prime[A[i]]:
            count += 1

    print(count)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 1. 約数を求める
    # 2. その約数が、いずれかの数値の倍数であるかどうかを確認する
    # 3. いずれかの数値の倍数である場合、その約数は除外する
    # 4. 除外した約数の数をカウントする
    # 5. 除外した約数の数が、入力数値の数と同じ数値である場合、その数値は、
    #    いずれの数値の倍数でないという条件を満たす
    # 6. その数値をカウントする
    # 7. 最後に、カウントした数値を出力する

    # 1. 約数を求める
    # 1.1. 最大値を求める
    max_a = max(a)
    # 1.2. 最大値の約数を求める
    # 1.2.1. 約数を格納するリスト
    divisor_list = []
    # 1.2.2. 約数を求める
    for i in range(1, max_a + 1):
        if i * i > max_a:
            break
        if max_a % i == 0:
            divisor_list.append(i)
            if i != max_a // i:
                divisor_list.append(max_a // i)
    # 1.2.3. 約数リストをソートする
    divisor_list.sort()
    # 1.3. 約数リストを逆順にする
    divisor_list = divisor_list[::-1]

    # 2. その約数が、いずれかの数値の倍数であるかどうかを確認する
    # 2.1. その約数が、い
