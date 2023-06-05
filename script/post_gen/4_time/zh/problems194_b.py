Synthesizing 10/10 solutions

=======
Suggestion 1

def get_min_time(N, A, B):
    min_time = float('inf')
    for i in range(N):
        for j in range(N):
            if i == j:
                min_time = min(min_time, A[i]+B[j])
            else:
                min_time = min(min_time, max(A[i], B[j]))
    return min_time

=======
Suggestion 2

def min_time(n, a, b):
    min_time = 1000000000000000000
    for i in range(n):
        for j in range(n):
            if i != j:
                if a[i] > b[j]:
                    if min_time > a[i]:
                        min_time = a[i]
                else:
                    if min_time > b[j]:
                        min_time = b[j]
            else:
                if min_time > a[i] + b[j]:
                    min_time = a[i] + b[j]
    return min_time

=======
Suggestion 3

def main():
    # 读取输入
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 计算结果
    result = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                time = A[i] + B[j]
            else:
                time = max(A[i], B[j])
            if time > result:
                result = time
    # 输出结果
    print(result)

=======
Suggestion 4

def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    ans = 1000000000000000
    for i in range(N):
        for j in range(N):
            if i == j:
                ans = min(ans, AB[i][0] + AB[j][1])
            else:
                ans = min(ans, max(AB[i][0], AB[j][1]))
    print(ans)

=======
Suggestion 5

def solve(n, lst):
    lst.sort(key=lambda x:x[0]+x[1])
    return lst[-1][0]+lst[-2][1]
n = int(input())
lst = []
for i in range(n):
    a,b = map(int, input().split())
    lst.append((a,b))
print(solve(n,lst))

=======
Suggestion 6

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        tmp = input().split()
        a.append(int(tmp[0]))
        b.append(int(tmp[1]))

    a.sort()
    b.sort()

    if a[-1] > b[-1]:
        print(a[-1])
    else:
        print(b[-1])

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    min_time = 10 ** 5
    for i in range(n):
        for j in range(n):
            if i == j:
                time = a[i] + b[j]
            else:
                time = max(a[i], b[j])
            if time < min_time:
                min_time = time
    print(min_time)

=======
Suggestion 8

def worktime(n, a, b):
    #a.sort()
    #b.sort()
    #print(a)
    #print(b)
    #if a[n-1] > b[n-1]:
    #    return a[n-1]
    #else:
    #    return b[n-1]
    time = 0
    for i in range(n):
        if a[i] > b[i]:
            time += a[i]
        else:
            time += b[i]
    return time

=======
Suggestion 9

def solve():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    ans = float("inf")
    for i in range(N):
        for j in range(N):
            if i == j:
                ans = min(ans, A[i] + B[j])
            else:
                ans = min(ans, max(A[i], B[j]))
    print(ans)
solve()

=======
Suggestion 10

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(min([max(A[i], B[j]) for i in range(N) for j in range(N)]))
