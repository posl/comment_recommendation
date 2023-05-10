Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        if b[i] >= a[i]:
            ans += a[i]
            a[i] = 0
            b[i] -= a[i]
        else:
            ans += b[i]
            a[i] -= b[i]
            b[i] = 0
        if b[i] >= a[i+1]:
            ans += a[i+1]
            a[i+1] = 0
            b[i] -= a[i+1]
        else:
            ans += b[i]
            a[i+1] -= b[i]
            b[i] = 0
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    count = 0
    for i in range(n):
        if a_list[i] <= b_list[i]:
            count += a_list[i]
            b_list[i] -= a_list[i]
            if a_list[i+1] <= b_list[i]:
                count += a_list[i+1]
                a_list[i+1] = 0
            else:
                count += b_list[i]
                a_list[i+1] -= b_list[i]
        else:
            count += b_list[i]
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        ans += min(a[i], b[i])
        b[i] -= min(a[i], b[i])
        ans += min(a[i+1], b[i])
        a[i+1] -= min(a[i+1], b[i])

    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    ans = 0
    for i in range(N):
        ans += min(A[i], B[i])
        if A[i] < B[i]:
            B[i] = B[i] - A[i]
            ans += min(A[i+1], B[i])
            A[i+1] = max(0, A[i+1] - B[i])
    print(ans)

main()

=======
Suggestion 5

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        if a[i] >= b[i]:
            ans += b[i]
            a[i] -= b[i]
            b[i] = 0
        else:
            ans += a[i]
            b[i] -= a[i]
            a[i] = 0
        if a[i+1] >= b[i]:
            ans += b[i]
            a[i+1] -= b[i]
            b[i] = 0
        else:
            ans += a[i+1]
            b[i] -= a[i+1]
            a[i+1] = 0
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        ans += min(a[i], b[i])
        a[i] -= min(a[i], b[i])
        b[i] -= min(a[i], b[i])
        ans += min(a[i+1], b[i])
        a[i+1] -= min(a[i+1], b[i])
        b[i] -= min(a[i+1], b[i])
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        if a[i] >= b[i]:
            ans += b[i]
            a[i] -= b[i]
        else:
            ans += a[i]
            b[i] -= a[i]
            if a[i+1] >= b[i]:
                ans += b[i]
                a[i+1] -= b[i]
            else:
                ans += a[i+1]
                a[i+1] = 0
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        ans += min(a[i], b[i])
        b[i] = max(0, b[i] - a[i])
        ans += min(a[i+1], b[i])
        a[i+1] = max(0, a[i+1] - b[i])

    print(ans)

=======
Suggestion 9

def main():
    # n = int(input())
    # a = list(map(int, input().split()))
    # b = list(map(int, input().split()))
    # print(a, b)
    n = 3
    a = [5, 6, 3, 8]
    b = [5, 100, 8]

    # a = [3, 5, 2]
    # b = [4, 5]
    # print(a, b)
    # a = [100, 1, 1]
    # b = [1, 100]
    # print(a, b)
    # n = 2
    # a = [3, 5, 2]
    # b = [4, 5]
    # print(a, b)
    # n = 2
    # a = [100, 1, 1]
    # b = [1, 100]
    # print(a, b)
    # n = 3
    # a = [5, 6, 3, 8]
    # b = [5, 100, 8]
    # print(a, b)
    # n = 3
    # a = [5, 6, 3, 8]
    # b = [5, 100, 8]
    # print(a, b)
    # n = 3
    # a = [5, 6, 3, 8]
    # b = [5, 100, 8]
    # print(a, b)
    # n = 3
    # a = [5, 6, 3, 8]
    # b = [5, 100, 8]
    # print(a, b)
    # n = 3
    # a = [5, 6, 3, 8]
    # b = [5, 100, 8]
    # print(a, b)
    # n = 3
    # a = [5, 6, 3, 8]
    # b = [5, 100, 8]
    # print(a, b)
    # n = 3
    # a = [5, 6, 3, 8]
    # b = [5, 100, 8

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        if a[i] <= b[i]:
            ans += a[i]
            b[i] -= a[i]
            if a[i+1] <= b[i]:
                ans += a[i+1]
                a[i+1] = 0
            else:
                ans += b[i]
                a[i+1] -= b[i]
        else:
            ans += b[i]
    print(ans)
