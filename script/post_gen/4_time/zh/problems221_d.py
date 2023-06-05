Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    days = []
    for i in range(n):
        a, b = map(int, input().split())
        days.append((a, 1))
        days.append((a + b, -1))
    days.sort()
    ans = [0] * (n + 1)
    num = 0
    last = 0
    for day, diff in days:
        ans[num] += day - last
        num += diff
        last = day
    print(*ans[1:])

=======
Suggestion 2

def main():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    #print(a, b)

    #print(max(a), max(b))
    #print(min(a), min(b))

    # 1. 生成一个列表，记录每一天有多少人登录
    # 2. 从中找出有k个人登录的天数
    # 3. 输出
    # 1.
    c = [0] * (max(a) + max(b) + 1)
    for i in range(n):
        for j in range(a[i], a[i] + b[i]):
            c[j] += 1
    #print(c)
    # 2.
    d = [0] * (n + 1)
    for i in range(len(c)):
        if c[i] > 0:
            d[c[i]] += 1
    #print(d)
    # 3.
    for i in range(1, n + 1):
        print(d[i], end=' ')
    print()

=======
Suggestion 3

def main():
    N = int(input())
    login = []
    for i in range(N):
        A, B = map(int, input().split())
        login.append([A, B])
    login.sort()
    login.append([10 ** 9 + 1, 0])
    ans = [0] * (N + 1)
    cnt = 0
    day = login[0][0]
    for i in range(N):
        if login[i][0] != day:
            ans[cnt] += login[i][0] - day
            day = login[i][0]
        cnt += login[i][1]
        if login[i + 1][0] != day:
            ans[cnt] += 1
    print(*ans[1:])

=======
Suggestion 4

def main():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    # print(ab)
    count = [0] * (10 ** 9 + 2)
    for i in range(n):
        count[ab[i][0]] += 1
        count[ab[i][0] + ab[i][1]] -= 1
    # print(count)
    for i in range(1, 10 ** 9 + 2):
        count[i] += count[i - 1]
    # print(count)
    ans = [0] * (n + 1)
    for i in range(1, 10 ** 9 + 1):
        ans[count[i]] += 1
    # print(ans)
    for i in range(1, n + 1):
        print(ans[i], end=" ")

=======
Suggestion 5

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    a.sort()
    b.sort()
    # print(a)
    # print(b)
    i = 0
    j = 0
    k = 0
    ans = [0]*n
    while i < n:
        if a[i] <= b[j]:
            k += 1
            i += 1
        else:
            k -= 1
            j += 1
        ans[k] += 1
    print(' '.join(map(str,ans)))

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    days = []
    for i in range(N):
        for j in range(B[i]):
            days.append(A[i]+j)
    #print(days)
    days.sort()
    #print(days)
    count = 0
    ans = []
    for i in range(len(days)-1):
        count += 1
        if days[i] != days[i+1]:
            ans.append(count)
            count = 0
    ans.append(count+1)
    #print(ans)
    for i in range(N):
        print(ans[i],end=' ')

=======
Suggestion 7

def read_data():
    n = int(input())
    a_list = []
    b_list = []
    for i in range(n):
        a, b = map(int, input().split())
        a_list.append(a)
        b_list.append(b)
    return n, a_list, b_list

=======
Suggestion 8

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

    # A = [1, 2, 3]
    # B = [2, 3, 1]

    # A = [1000000000, 1000000000]
    # B = [1000000000, 1000000000]

    # A = [1, 2, 3, 4, 5, 6]
    # B = [2, 3, 1, 1, 1, 1]

    # A = [1, 2, 3, 4, 5, 6]
    # B = [1, 1, 1, 1, 1, 1]

    # A = [1, 2, 3, 4, 5, 6]
    # B = [6, 5, 4, 3, 2, 1]

    # A = [1, 2, 3, 4, 5, 6]
    # B = [1, 2, 3, 4, 5, 6]

    # A = [1, 2, 3, 4, 5, 6]
    # B = [2, 3, 4, 5, 6, 7]

    # A = [1, 2, 3, 4, 5, 6]
    # B = [1, 3, 5, 7, 9, 11]

    # A = [1, 2, 3, 4, 5, 6]
    # B = [1, 2, 4, 8, 16, 32]

    # A = [1, 2, 3, 4, 5, 6]
    # B = [1, 2, 3, 4, 5, 7]

    # A = [1, 2, 3, 4, 5, 6]
    # B = [1, 2, 3,

=======
Suggestion 9

def problems221_d():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    ans = [0] * (n + 1)
    for i in range(n):
        ans[a[i]] += 1
        ans[a[i] + b[i]] -= 1
    for i in range(1, n + 1):
        ans[i] += ans[i - 1]
    ans.pop(0)
    print(*ans)
    return

problems221_d()

=======
Suggestion 10

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    #print(a)
    #print(b)
    #print(n)
    #print(len(a))
    #print(len(b))
    a_b = []
    for i in range(n):
        a_b.append([a[i], b[i]])
    #print(a_b)
    #print(a_b[0][0])
    #print(a_b[0][1])
    #print(a_b[1][0])
    #print(a_b[1][1])
    #print(a_b[2][0])
    #print(a_b[2][1])
    a_b.sort()
    #print(a_b)
    #print(a_b[0][0])
    #print(a_b[0][1])
    #print(a_b[1][0])
    #print(a_b[1][1])
    #print(a_b[2][0])
    #print(a_b[2][1])
    d = [0] * n
    #print(d)
    for i in range(n):
        d[i] = [0, 0]
    #print(d)
    #print(d[0][0])
    #print(d[0][1])
    #print(d[1][0])
    #print(d[1][1])
    #print(d[2][0])
    #print(d[2][1])
    for i in range(n):
        d[i][0] = a_b[i][0]
        d[i][1] = a_b[i][0] + a_b[i][1] - 1
    #print(d)
    #print(d[0][0])
    #print(d[0][1])
    #print(d[1][0])
    #print(d[1][1])
    #print(d[2][0])
    #print(d[2][1])
    #print(d[0][0])
    #print(d[0][1])
    #print(d[1][0])
    #print(d[1][1])
    #print(d[2][0])
    #print(d[2][1])
    #print(d[0][0])
    #print(d[0][
