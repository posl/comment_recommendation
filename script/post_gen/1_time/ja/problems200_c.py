Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if (A[i] - A[j]) % 200 == 0:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] - a[j]) % 200 == 0:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))

    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if (A[i] - A[j]) % 200 == 0:
                count += 1

    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = [0] * 200
    for i in range(N):
        cnt[A[i] % 200] += 1
    ans = 0
    for i in range(200):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]
    c = [0] * 200
    for a in A:
        c[a] += 1
    ans = 0
    for i in range(200):
        ans += c[i] * (c[i] - 1) // 2
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] - A[j] == 0:
                count += 1
    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a%200 for a in A]
    #print(A)
    d = dict()
    for a in A:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
    #print(d)
    ans = 0
    for k in d:
        ans += d[k]*(d[k]-1)//2
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]
    #print(A)

    dict = {}
    for a in A:
        if a in dict:
            dict[a] += 1
        else:
            dict[a] = 1
    #print(dict)

    ans = 0
    for d in dict:
        ans += dict[d] * (dict[d] - 1) // 2
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0

    for i in range(N-1):
        cnt = 0
        for j in range(i+1, N):
            if (A[j] - A[i]) % 200 == 0:
                cnt += 1
            else:
                break
        ans += cnt * (cnt - 1) // 2
    print(ans)
