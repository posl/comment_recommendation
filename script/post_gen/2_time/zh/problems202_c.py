Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    count = 0
    for i in range(1, n+1):
        count += b[c[i-1]-1] == a[i-1]

    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    b_count = [0] * n
    for i in range(n):
        b_count[b[c[i] - 1] - 1] += 1

    ans = 0
    for i in range(n):
        ans += b_count[a[i] - 1]

    print(ans)

=======
Suggestion 3

def problem202_c():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    a_dict = {}
    b_dict = {}
    c_dict = {}
    for i in range(n):
        a_dict[i] = a[i]
        b_dict[i] = b[i]
        c_dict[i] = c[i]
    a_dict = sorted(a_dict.items(), key=lambda x:x[1])
    b_dict = sorted(b_dict.items(), key=lambda x:x[1])
    c_dict = sorted(c_dict.items(), key=lambda x:x[1])
    count = 0
    for i in range(n):
        for j in range(n):
            if a_dict[i][1] == b_dict[c_dict[j][1]-1][1]:
                count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    a.sort()
    b.sort()
    c.sort()
    ans = 0
    for i in range(n):
        ans += bisect.bisect_left(a, b[c[i]-1])*(n-bisect.bisect_right(b, b[c[i]-1]))
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x: int(x) - 1, input().split()))
    count = 0
    for i in range(n):
        count += b[c[a[i] - 1]]
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda i: int(i) - 1, input().split()))

    d = [0] * n
    for i in range(n):
        d[c[i]] += 1

    ans = 0
    for i in range(n):
        ans += d[b[i] - 1]

    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    d = [0]*n
    for i in range(n):
        d[c[i]-1] += 1
    ans = 0
    for i in range(n):
        ans += d[b[a[i]-1]-1]
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    
    cnt = 0
    for i in range(n):
        cnt += b.count(c[a[i]-1])
    print(cnt)

main()

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    # for i in range(n):
    #     a[i] -= 1
    #     b[i] -= 1
    #     c[i] -= 1

    # a.sort()
    # b.sort()
    # c.sort()

    # ans = 0
    # for i in range(n):
    #     ans += (bisect.bisect_left(a, b[c[i]]) * (n - bisect.bisect_right(b, c[i])))

    # print(ans)

    # a = [a[i] for i in c]
    # b = [b[i] for i in c]

    # a.sort()
    # b.sort()

    # ans = 0
    # for i in range(n):
    #     ans += (bisect.bisect_left(a, b[i]) * (n - bisect.bisect_right(b, i)))

    # print(ans)

    # a = [a[i] for i in c]
    # b = [b[i] for i in c]

    # a.sort()
    # b.sort()

    # ans = 0
    # for i in range(n):
    #     ans += (bisect.bisect_left(a, b[i]) * (n - bisect.bisect_right(b, i)))

    # print(ans)

    # a = [a[i] for i in c]
    # b = [b[i] for i in c]

    # a.sort()
    # b.sort()

    # ans = 0
    # for i in range(n):
    #     ans += (bisect.bisect_left(a, b[i]) * (n - bisect.bisect_right(b, i)))

    # print(ans)

    # a = [a[i] for i in c]
    # b = [b[i] for i in c]

    # a.sort()
    # b.sort()

    # ans = 0
    # for i in range(n):
    #     ans += (bisect.bisect_left(a, b[i]) * (n - bisect.bisect_right(b, i)))

    # print(ans)

    # a =

=======
Suggestion 10

def main():
    N = int(input())
    A = input().split()
    B = input().split()
    C = input().split()
    for i in range(N):
        A[i] = int(A[i])
        B[i] = int(B[i])
        C[i] = int(C[i])
    count = 0
    for i in range(N):
        count += B.count(A[C[i]-1])
    print(count)
