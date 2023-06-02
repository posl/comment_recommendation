Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a_b = []
    for _ in range(n):
        a_b.append(list(map(int, input().split())))
    a_b.sort(key=lambda x: x[0])
    a_b.sort(key=lambda x: x[1])
    # print(a_b)
    a = [x[0] for x in a_b]
    b = [x[1] for x in a_b]
    # print(a)
    # print(b)
    a_b = []
    for i in range(n):
        if i == 0:
            a_b.append([a[i], b[i]])
        else:
            if a[i] == a[i-1]:
                a_b[-1][1] += b[i]
            else:
                a_b.append([a[i], b[i]])
    # print(a_b)
    b = [x[1] for x in a_b]
    # print(b)
    ans = []
    for i in range(1, n+1):
        ans.append(b.count(i))
    print(' '.join(map(str, ans)))

=======
Suggestion 2

def get_input():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    return N, A, B

=======
Suggestion 3

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)

    d = [0 for i in range(10**9+1)]

    for i in range(n):
        d[a[i]] += 1
        d[a[i]+b[i]] -= 1

    for i in range(1, 10**9+1):
        d[i] += d[i-1]

    for i in range(1, n+1):
        ans = 0
        for j in range(10**9+1):
            if d[j] == i:
                ans += 1
        print(ans, end=' ')

=======
Suggestion 4

def main():
    n = int(input())
    dict = {}
    for i in range(n):
        a,b = map(int,input().split())
        for j in range(a,a+b):
            if j in dict:
                dict[j] += 1
            else:
                dict[j] = 1
    for i in range(1,n+1):
        if i in dict:
            print(dict[i],end=" ")
        else:
            print(0,end=" ")

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A, B)
    C = [0] * (10**9 + 1)
    for i in range(N):
        C[A[i]] += 1
        C[A[i]+B[i]] -= 1
    #print(C)
    for i in range(1, 10**9 + 1):
        C[i] += C[i-1]
    #print(C)
    D = [0] * (N + 1)
    for i in range(1, 10**9 + 1):
        D[C[i]] += 1
    print(" ".join(map(str, D[1:])))

main()

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(N)

    #C = [0] * (10 ** 9 + 2)
    C = [0] * (10 ** 9 + 2)
    for i in range(N):
        #C[A[i]] += 1
        C[A[i]] += 1
        #C[A[i] + B[i]] -= 1
        C[A[i] + B[i]] -= 1

    #print(C)
    for i in range(10 ** 9 + 1):
        C[i + 1] += C[i]

    #print(C)
    for i in range(10 ** 9 + 1):
        if C[i] != 0:
            print(C[i], end=" ")
    print()

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    for i in range(n):
        a[i] -= 1
    d = [0] * (2 * 10**9 + 2)
    for i in range(n):
        d[a[i]] += 1
        d[a[i] + b[i]] -= 1
    for i in range(1, 2 * 10**9 + 2):
        d[i] += d[i - 1]
    e = [0] * (n + 1)
    for i in range(2 * 10**9 + 1):
        if d[i] > 0:
            e[d[i]] += 1
    for i in range(1, n + 1):
        print(e[i], end=" ")
    print()

=======
Suggestion 8

def problems221_d():
    pass

=======
Suggestion 9

def main():
    n = int(input())
    a_b = [list(map(int, input().split())) for _ in range(n)]
    #print(a_b)
    #print(a_b[0])
    #print(a_b[0][0])
    #print(a_b[0][1])
    #print(a_b[1])
    #print(a_b[1][0])
    #print(a_b[1][1])
    #print(a_b[2])
    #print(a_b[2][0])
    #print(a_b[2][1])
    #print(a_b[0][1])
    #print(a_b[1][0])
    #print(a_b[1][1])
    #print(a_b[2][0])
    #print(a_b[2][1])
    #print(a_b[0][1])
    #print(a_b[1][1])
    #print(a_b[2][1])
    #print(a_b[0][1])
    #print(a_b[1][1])
    #print(a_b[2][1])
    #print(a_b[0][1])
    #print(a_b[1][1])
    #print(a_b[2][1])
    #print(a_b[0][1])
    #print(a_b[1][1])
    #print(a_b[2][1])
    #print(a_b[0][1])
    #print(a_b[1][1])
    #print(a_b[2][1])
    #print(a_b[0][1])
    #print(a_b[1][1])
    #print(a_b[2][1])
    #print(a_b[0][1])
    #print(a_b[1][1])
    #print(a_b[2][1])
    #print(a_b[0][1])
    #print(a_b[1][1])
    #print(a_b[2][1])
    #print(a_b[0][1])
    #print(a_b[1][1])
    #print(a_b[2][1])

    #print(a_b[0][0])
    #print(a_b[1][0])
    #print(a_b[2][0])
    #print(a_b[0][0])
    #print(a_b[1][0])
    #print(a_b[2][0])
    #print

=======
Suggestion 10

def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    #print(A)
    #print(B)

    #计算每个玩家的登录日
    login_days = []
    for i in range(N):
        login_days.append([A[i], A[i]+B[i]-1])

    #print(login_days)

    #将登录日按照登录日的开始时间排序
    login_days.sort()

    #print(login_days)

    #计算每个玩家的登录日是否有重叠
    overlap = []
    for i in range(N-1):
        if login_days[i][1] >= login_days[i+1][0]:
            overlap.append([login_days[i][1], login_days[i+1][0]])

    #print(overlap)

    #计算每个玩家的登录日是否有重叠
    #count = 0
    #for i in range(N-1):
    #    if login_days[i][1] >= login_days[i+1][0]:
    #        count += 1
    #print(count)

    #计算每个玩家的登录日是否有重叠
    count = 0
    for i in range(len(overlap)-1):
        if overlap[i][0] >= overlap[i+1][1]:
            count += 1
    print(count)
