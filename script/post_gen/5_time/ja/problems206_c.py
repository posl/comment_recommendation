Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_ints():
    return map(int, input().split())

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] != A[j]:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    c = [0] * (n + 1)
    for i in range(n):
        ans += i - c[a[i]]
        c[a[i]] += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] != a[j]:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    A.sort()
    #print(A)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] != A[j]:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += (n-i-1)
    for i in range(1,n):
        if a[i-1] == a[i]:
            ans -= 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = {}
    for i in range(n):
        if a[i] in count:
            count[a[i]] += 1
        else:
            count[a[i]] = 1
    ans = 0
    for i in count:
        ans += count[i] * (count[i] - 1) // 2
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] == A[j]:
                continue
            else:
                count += 1
    print(count)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = 1
        else:
            d[a[i]] += 1
    print(sum([d[i] * (d[i] - 1) // 2 for i in d]))
