Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i == 0 or a[i] != a[i-1]:
            for j in range(i+1, n):
                if a[j] % a[i] == 0:
                    break
            else:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    count = 0
    for i in range(N):
        if i == 0:
            count += 1
        elif A[i] % A[i-1] != 0:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    for i in range(n):
        if i == 0 or a[i] != a[i-1]:
            if i == n-1 or a[i] != a[i+1]:
                cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    cnt = 0
    for i in range(n):
        if a[i] != a[i+1]:
            cnt += 1
    print(cnt)

=======
Suggestion 5

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    i = 1
    while i < N:
        if A[i] % A[0] == 0:
            A.pop(i)
            N -= 1
        else:
            i += 1

    print(N)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A_max = A[-1]
    A_count = [0] * (A_max + 1)
    for a in A:
        A_count[a] += 1
    A_count_div = [0] * (A_max + 1)
    for a in A:
        for i in range(2 * a, A_max + 1, a):
            A_count_div[i] += 1
    A_count_div = [N - a - 1 for a in A_count_div]
    ans = sum([a * b for a, b in zip(A_count, A_count_div)])
    print(ans)
    return()

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    max_num = A[0]
    count = 0
    for i in range(1, N):
        if max_num % A[i] != 0:
            count += 1
    print(count + 1)

=======
Suggestion 9

def myCode():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 1
    for i in range(1, n):
        if a[i] % a[0] != 0:
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    a = set(a)
    a = sorted(a)
    a = list(reversed(a))
    a = set(a)
    a = sorted(a)
    a = list(reversed(a))
    print(len(a))
