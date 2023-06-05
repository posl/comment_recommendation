Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N = int(input())
A = list(map(int, input().split()))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    d = {}
    for i in range(n):
        for j in range(n):
            if a[j] == 0:
                continue
            if a[i] % a[j] == 0:
                cnt += d.get(a[i] // a[j], 0)
    for i in range(n):
        d[a[i]] = d.get(a[i], 0) + 1
    print(cnt)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    ans = 0
    for i in range(n):
        for j in range(n):
            if a[j] == 0:
                continue
            if a[i] % a[j] != 0:
                continue
            if a[i] // a[j] in d:
                ans += d[a[i] // a[j]]
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    dic = {}
    for i in range(n):
        if a[i] in dic:
            dic[a[i]] += 1
        else:
            dic[a[i]] = 1
    for i in range(n):
        for j in range(n):
            if a[i] % a[j] == 0:
                if a[i] // a[j] in dic:
                    cnt += dic[a[i] // a[j]]
    print(cnt)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] % a[j] == 0:
                for k in range(j+1, n):
                    if a[j] % a[k] == 0:
                        cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(N):
        for j in range(N):
            if A[i] % A[j] == 0:
                for k in range(N):
                    if A[j] % A[k] == 0:
                        cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int,input().split()))
    count = 0
    for i in range(1,n):
        for j in range(i):
            if a[i] == a[j]:
                count += 1
    print(count)

=======
Suggestion 8

def solve(n, arr):
    # Write your code here
    ans = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                if arr[i] * arr[j] == arr[k]:
                    ans += 1
    return ans

n = int(input())
arr = list(map(int, input().split()))
print(solve(n, arr))

=======
Suggestion 9

def solution():
    n = int(input())
    a = list(map(int,input().split()))
    a.insert(0,0)
    cnt = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if a[i]%a[j]==0:
                cnt += a.index(a[i]//a[j])
    print(cnt)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = 1
        else:
            d[a[i]] += 1
    ans = 0
    for i in range(n):
        for j in range(n):
            if a[j] != 0 and a[i] % a[j] == 0:
                if a[i] // a[j] in d:
                    ans += d[a[i] // a[j]]
    print(ans)
