Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if (A[i]-A[j])%200 == 0:
                cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if (A[i] - A[j]) % 200 == 0:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (a[i] - a[j]) % 200 == 0:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N-1):
        for j in range(i+1,N):
            if (A[i] - A[j]) % 200 == 0:
                ans += 1
    print(ans)

main()

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            if (a[i] - a[j]) % 200 == 0:
                count += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]
    from collections import Counter
    c = Counter(A)
    ans = 0
    for v in c.values():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [x % 200 for x in a]
    cnt = [0] * 200
    for i in a:
        cnt[i] += 1
    ans = 0
    for i in cnt:
        ans += i * (i - 1) // 2
    print(ans)

=======
Suggestion 8

def count200(N, A):
    # 200で割った余りをカウント
    C = [0] * 200
    for a in A:
        C[a % 200] += 1
    # 余りごとに組み合わせを数える
    ans = 0
    for c in C:
        ans += c * (c - 1) // 2
    return ans
