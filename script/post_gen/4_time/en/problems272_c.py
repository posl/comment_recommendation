Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) % 2 == 0:
                print(a[i] + a[j])
                return
    print(-1)

=======
Suggestion 2

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort(reverse=True)
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) % 2 == 0:
                print(a[i] + a[j])
                return
    print(-1)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    max_even = -1
    for i in range(N):
        for j in range(i+1, N):
            if (A[i] + A[j]) % 2 == 0:
                if A[i] + A[j] > max_even:
                    max_even = A[i] + A[j]
                break
    print(max_even)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    result = -1
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) % 2 == 0:
                result = max(result, a[i] + a[j])
            else:
                break
    print(result)

=======
Suggestion 5

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[-1] % 2 == 0:
        print(a[-1])
    else:
        for i in range(n-1):
            if a[i] % 2 == 0 and a[i] + 1 == a[i+1]:
                print(a[-1])
                break
        else:
            print(-1)
solve()

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    even = []
    for i in range(N):
        if A[i]%2 == 0:
            even.append(A[i])
    if len(even) == 0:
        print(-1)
    else:
        print(even[0])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    s = set()
    for i in range(N):
        for j in range(i+1, N):
            if (A[i]+A[j])%2==0:
                s.add(A[i]+A[j])
                break
    if len(s)==0:
        print(-1)
    else:
        print(max(s))

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()

    ans = -1
    for i in range(N):
        for j in range(i + 1, N):
            if (A[i] + A[j]) % 2 == 0:
                ans = max(ans, A[i] + A[j])

    print(ans)

=======
Suggestion 9

def check_even_pair(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if (array[i] + array[j]) % 2 == 0:
                return array[i] + array[j]
    return -1

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * 1000001
    for i in range(n):
        b[a[i]] += 1
    if b[0] > 1:
        print(0)
        return
    for i in range(1, 1000001):
        if b[i] > 1:
            print(i * 2)
            return
    for i in range(1, 1000001):
        if b[i] > 0:
            for j in range(i + i, 1000001, i):
                if b[j] > 0:
                    print(j)
                    return
    print(-1)
    return
