Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        x = a[i]
        for j in range(i, n):
            x = min(x, a[j])
            ans = max(ans, x * (j - i + 1))
    print(ans)
main()

=======
Suggestion 2

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    for l in range(N):
        x = A[l]
        for r in range(l, N):
            x = min(x, A[r])
            ans = max(ans, x * (r - l + 1))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(1, 10**5+1):
        l = 0
        r = 0
        while True:
            while r < N and A[r] >= x:
                r += 1
            if r == N:
                break
            if l == r:
                l += 1
                r += 1
            else:
                ans = max(ans, x*(r-l))
                l += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    ans = 0
    for i in range(N):
        x = A[i]
        for j in range(i, N):
            x = min(x, A[j])
            ans = max(ans, x * (j - i + 1))
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for x in range(1, 10**5+1):
        cnt = 0
        for i in range(n):
            if cnt == 0:
                if a[i] >= x:
                    cnt += 1
            else:
                if a[i] >= x:
                    cnt += 1
                else:
                    ans = max(ans, cnt*x)
                    cnt = 0
        ans = max(ans, cnt*x)
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0

    for x in range(1, 10**5+1):
        l = 0
        r = 0
        while l < N:
            while r < N and A[r] >= x:
                r += 1
            ans = max(ans, x * (r - l))
            l = r + 1
            r = l

    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        max_a = 0
        for j in range(i, N):
            max_a = max(max_a, A[j])
            ans = max(ans, max_a * (j - i + 1))
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for x in range(1, 100001):
        l = 0
        r = 0
        while l < N:
            while r < N and a[r] >= x:
                r += 1
            ans = max(ans, x * (r - l))
            l = r
            r = r + 1
    print(ans)

=======
Suggestion 9

def main():
    #input
    N = int(input())
    A = list(map(int, input().split()))

    #compute
    ans = 0
    for x in range(1, 10**5+1):
        l = 0
        r = 0
        for i in range(N):
            if A[i] >= x:
                r = i
                if l == 0:
                    l = i
                ans = max(ans, (r-l+1)*x)

    #output
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # A[i]を選ぶか選ばないかの2通りで、全ての選び方を試す
    # 2**N通りになる
    # ただし、A[i]を選んだときに、A[i]より小さい数を選んではいけない
    # そのため、A[i]より小さい数を選んだときには、その選び方は無効とする
    # そのため、A[i]を選ぶときに、A[i]より小さい数を選んでいるかどうかをチェックする
    # A[i]より小さい数を選んでいる場合は、その選び方は無効とする
    # そのため、A[i]より小さい数を選んでいるかどうかをチェックする
    # このチェックは、A[i]より小さい数を選んでいるかどうかをチェックするために、
    # A[i]より小さい数を選んでいる場合は、その選び方は無効とする
    # そのため、A[i]より小さい数を選んでいるかどうかをチェックする
    # このチェックは、A[i]より小さい数を選んでいるかどうかをチェックするために、
    # A[i]より小さい数を選んでいる場合は、その選び方は無効とする
    # そのため、A[i]より小さい数を選んでいるかどうかをチェックする
    # このチェックは、A[i]より小さい数を選んでいるかど
