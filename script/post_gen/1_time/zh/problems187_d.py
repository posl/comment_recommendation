Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort(reverse=True)
    B.sort(reverse=True)
    #print(A)
    #print(B)
    cnt = 0
    for i in range(N):
        if A[i] > B[i]:
            cnt += 1
    print(cnt)

=======
Suggestion 2

def solve():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append([int(x) for x in input().split()])
    AB.sort(key=lambda x: x[0] + x[1], reverse=True)
    # print(AB)
    count = 0
    for i in range(N):
        if i % 2 == 0:
            count += AB[i][0]
        else:
            count -= AB[i][1]
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a_sum = sum(a)
    b_sum = sum(b)
    if a_sum > b_sum:
        print(0)
        return
    else:
        # a_sum <= b_sum
        # 为了获得比青木更多的选票，高桥至少需要在多少个城镇发表演讲？
        # 高桥在哪些城镇发表演讲，是关键
        # 高桥在哪些城镇发表演讲，就有哪些城镇的青木选民投票给了高桥
        # 高桥在哪些城镇发表演讲，就有哪些城镇的高桥选民投票给了高桥
        # 高桥在哪些城镇发表演讲，就有哪些城镇的高桥选民投票给了青木
        # 高桥在哪些城镇发表演讲，就有哪些城镇的青木选民投票给了青木
        # 高桥在哪些城镇发表演讲，就有哪些城镇的高桥选民没有投票
        # 高桥在哪些城镇发表演讲，就有哪些城镇的青木选民没有投票
        # 高桥在哪些城镇发表演讲，就有哪些城镇的高桥选民投票给了高桥，而青木选民没有投票
        # 高桥在哪些城镇发表演讲，就有哪些城镇的高桥选民投票给了青木，而青木选民没有投票

=======
Suggestion 4

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # print(A)
    # print(B)

    # 有一个镇，只要高桥发表演讲，就能赢，否则输
    if N == 1:
        print(1)
        return

    # 有两个镇，只要高桥在两个镇中的一个发表演讲，就能赢，否则输
    if N == 2:
        if A[0] + B[0] < A[1] + B[1]:
            print(1)
        else:
            print(2)
        return

    # 有三个或更多镇，高桥必须在至少三个镇中的一个发表演讲，才能赢
    # 从最后一个镇开始，如果高桥在该镇发表演讲，那么该镇的所有选民都会投票给高桥
    # 否则，该镇的所有亲高桥的选民都会投票给青木
    # 那么，问题转化为：有N个镇，每个镇有A_i支持青木的选民和B_i支持高桥的选民，高桥至少需要在多少个镇发表演讲，才能赢
    # 由于高桥必须在至少三个镇中的一个发表演讲，才能赢，所以高桥至少需要在三个镇中的一个发表演讲，才能赢
    # 那么，问题转化为：有N个镇，每个镇有A_i支持青木的选民和B_i支持高桥的选民，高桥至少需要在多少个镇中的一个发表演讲，才能赢

=======
Suggestion 5

def solve():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    a.sort(reverse=True)
    b.sort(reverse=True)
    i = 0
    j = 0
    cnt = 0
    while i < n:
        if a[i] > b[j]:
            cnt += 1
            i += 1
            j += 1
        else:
            i += 1
    print(cnt)

=======
Suggestion 6

def solve():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    res = 0
    for i in range(n-1,-1,-1):
        a[i] += res
        if a[i]%b[i] == 0:
            continue
        res += b[i] - a[i]%b[i]
    print(res)
solve()

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    c = []
    for i in range(n):
        c.append(a[i] + b[i])
    c.sort(reverse=True)
    sum = 0
    for i in range(n):
        if i % 2 == 0:
            sum += c[i]
        else:
            sum -= c[i]
    print(sum)

=======
Suggestion 8

def solve():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort(reverse=True)
    b.sort(reverse=True)
    ans = 0
    for i in range(n):
        if a[i] > b[i]:
            ans += 1
    print(ans)

solve()

=======
Suggestion 9

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    c = []
    for i in range(n):
        c.append(a[i] + b[i])
    d = []
    for i in range(n):
        d.append(a[i] - b[i])
    c.sort()
    d.sort()
    print(min(c[n - 1], sum(d[n - 1:n + 1])))
main()

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
    A.sort(reverse=True)
    B.sort(reverse=True)
    ans = 0
    for i in range(N):
        if A[i] > B[i]:
            ans += 1
    print(ans)
