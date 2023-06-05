Synthesizing 10/10 solutions

=======
Suggestion 1

def sum1(A):
    sum = 0
    for i in A:
        sum += i
    return sum

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]

    dic = {}
    for a in A:
        dic[a] = dic.get(a, 0) + 1

    ans = sum(A)
    for b, c in BC:
        if b in dic:
            ans += (c - b) * dic[b]
            dic[c] = dic.get(c, 0) + dic[b]
            dic[b] = 0
        print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    q = int(input())
    bc = [input().split() for _ in range(q)]
    b = [int(i[0]) for i in bc]
    c = [int(i[1]) for i in bc]
    print(sum(a))
    for i in range(q):
        print(sum(a) - a.count(b[i]) * (b[i] - c[i]))

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = [0] * q
    c = [0] * q
    for i in range(q):
        b[i], c[i] = map(int, input().split())
    sum_a = sum(a)
    for i in range(q):
        sum_a = sum_a - a[b[i] - 1] * (b[i] - c[i]) + a[b[i] - 1] * c[i]
        print(sum_a)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())

    sum = 0
    for i in range(n):
        sum += a[i]

    for i in range(q):
        b, c = map(int, input().split())
        sum += (c - b) * a.count(b)
        print(sum)
        a = [c if x == b else x for x in a]

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = [0] * q
    c = [0] * q
    for i in range(q):
        b[i], c[i] = map(int, input().split())

    sum = 0
    for i in range(n):
        sum += a[i]

    for i in range(q):
        sum = sum - a[b[i] - 1] + c[i] * b[i]
        print(sum)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    S = sum(A)
    for i in range(Q):
        B, C = BC[i]
        S += (C - B) * A.count(B)
        print(S)
        A = [C if a == B else a for a in A]
    return

main()

=======
Suggestion 8

def main():
    #读取输入数据
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]

    #计算并输出答案
    print(sum(A))
    for i in range(Q):
        b, c = BC[i]
        print(sum(A) - A.count(b) * (b - c))

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = []
    c = []
    for _ in range(q):
        b_, c_ = map(int, input().split())
        b.append(b_)
        c.append(c_)
    sum_a = sum(a)
    for i in range(q):
        sum_a = sum_a + (c[i] - b[i]) * a.count(b[i])
        print(sum_a)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]

    sumA = sum(A)
    dic = {}
    for i in range(N):
        if A[i] not in dic:
            dic[A[i]] = 1
        else:
            dic[A[i]] += 1

    for i in range(Q):
        sumA += (BC[i][1] - BC[i][0]) * dic.get(BC[i][0], 0)
        if BC[i][1] in dic:
            dic[BC[i][1]] += dic.get(BC[i][0], 0)
            dic[BC[i][0]] = 0
        else:
            dic[BC[i][1]] = dic.get(BC[i][0], 0)
            dic[BC[i][0]] = 0
        print(sumA)
