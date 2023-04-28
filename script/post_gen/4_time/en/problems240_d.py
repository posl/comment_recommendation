Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (2 * 10 ** 5 + 1)
    for a in A:
        B[a] += 1
    ans = 0
    for i in range(1, 2 * 10 ** 5 + 1):
        ans = max(ans, B[i - 1] + B[i] + B[i + 1])
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (2 * 10 ** 5 + 1)
    for i in range(n):
        b[a[i]] += 1
    ans = 0
    for i in range(2 * 10 ** 5 + 1):
        ans += b[i] % 2
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = [0] * (2 * 10 ** 5 + 1)
    for i in range(n):
        count[a[i]] += 1
    ans = 0
    for i in range(2 * 10 ** 5 + 1):
        ans += count[i] * (count[i] - 1) // 2
    for i in range(n):
        print(ans - count[a[i]] + 1)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = [0] * (2 * 10 ** 5 + 1)
    ans = 0
    for i in range(n):
        count[a[i]] += 1
        if count[a[i]] == 1:
            ans += 1
        else:
            ans -= 1
        print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0]*(2*10**5+1)
    c = 0
    for i in a:
        b[i] += 1
        if b[i] == i:
            c += 1
        elif b[i] > i:
            b[i] = 0
    for i in a:
        if b[i] == 0:
            print(c)
        else:
            print(c+1)

=======
Suggestion 6

def main():
    N = int(input())
    a = list(map(int, input().split()))
    d = {}
    d[0] = 1
    for i in range(N):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
        if a[i]-1 in d:
            d[a[i]-1] += 1
        else:
            d[a[i]-1] = 1
        if a[i]+1 in d:
            d[a[i]+1] += 1
        else:
            d[a[i]+1] = 1
    print(max(d.values()))

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0 for i in range(N)]
    for i in range(N):
        B[i] = A[i] - 1
    C = [0 for i in range(N)]
    for i in range(N):
        C[B[i]] += 1
    for i in range(N):
        print(C[i])

=======
Suggestion 8

def main():
    N = int(input())
    balls = list(map(int, input().split()))
    ans = [0] * N
    ans[0] = 1
    for i in range(1, N):
        ans[i] = ans[i-1]
        if balls[i-1] == ans[i]:
            ans[i] += 1
    for i in range(N):
        print(ans[i])

main()

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        d[i] = a[i]
    b = []
    for i in range(n):
        b.append(0)
    for i in range(n):
        if d[i] not in b:
            b.append(d[i])
        else:
            b.remove(d[i])
            b.remove(d[i])
    print(len(b))

=======
Suggestion 10

def check_consecutive(arr, n):
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            return True
    return False
