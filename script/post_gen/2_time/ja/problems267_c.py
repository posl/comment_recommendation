Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(m):
        ans += (i + 1) * a[i]
    tmp = ans
    for i in range(n - m):
        tmp = tmp - a[i] + a[i + m]
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-M+1):
        ans = max(ans, sum(A[i:i+M]) + sum(range(1, M+1)))
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-M+1):
        ans += sum(A[i:i+M]) * (M-i)
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(M):
        B[i] = A[i]
    for i in range(M, N):
        B[i] = B[i - 1] + A[i]
    ans = 0
    for i in range(M, N):
        ans = max(ans, B[i] - B[i - M])
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-m+1):
        ans = max(ans, sum(a[i:i+m])*m-sum(a[i:i+m]))
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 0
    for i in range(m):
        ans += (i+1) * a[i]
    print(ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-m+1):
        ans += sum(a[i:i+m]) * (i+1)
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-M+1):
        ans = max(ans, sum((i+1)*A[i+j] for j in range(M)))
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M)
    #print(A)

    #連続部分列の総和を計算する
    #連続部分列の長さが2の場合： 1*3 + 2*1 = 5
    #連続部分列の長さが3の場合： 1*3 + 2*1 + 3*(-4) = -1
    #連続部分列の長さが4の場合： 1*3 + 2*1 + 3*(-4) + 4*1 = 3
    #連続部分列の長さが5の場合： 1*3 + 2*1 + 3*(-4) + 4*1 + 5*(-5) = -2
    #連続部分列の長さが6の場合： 1*3 + 2*1 + 3*(-4) + 4*1 + 5*(-5) + 6*9 = 7
    #連続部分列の長さが7の場合： 1*3 + 2*1 + 3*(-4) + 4*1 + 5*(-5) + 6*9 + 7*(-2) = 5
    #連続部分列の長さが8の場合： 1*3 + 2*1 + 3*(-4) + 4*1 + 5*(-5) + 6*9 + 7*(-2) + 8*6 = 11
    #連続部分列の長さが9の場合： 1*3 + 2*1 + 3*(-4) + 4*1 + 5*(-5) + 6*9 + 7*(-2) + 8*6 + 9*(-5) = 6
    #連続部分列の長さが10の場合：1*3 + 2*1 + 3*(-4) + 4*1 + 5*(-

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    # b = [a[i] * (i + 1) for i in range(n)]
    # print(b)
    # c = [a[i] * (n - i) for i in range(n)]
    # print(c)
    # sum_b = [0]
    # sum_c = [0]
    # for i in range(n):
    #     sum_b.append(sum_b[i] + b[i])
    #     sum_c.append(sum_c[i] + c[i])
    # print(sum_b)
    # print(sum_c)
    # ans = 0
    # for i in range(n - m + 1):
    #     ans = max(ans, sum_c[i] + sum_b[i + m] - sum_b[i] - sum_c[i + m])
    # print(ans)

    sum_b = [0]
    sum_c = [0]
    for i in range(n):
        sum_b.append(sum_b[i] + a[i] * (i + 1))
        sum_c.append(sum_c[i] + a[i] * (n - i))
    # print(sum_b)
    # print(sum_c)
    ans = 0
    for i in range(n - m + 1):
        ans = max(ans, sum_c[i] + sum_b[i + m] - sum_b[i] - sum_c[i + m])
    print(ans)
