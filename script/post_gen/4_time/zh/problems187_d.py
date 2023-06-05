Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[0] + x[1], reverse=True)
    sumA = sum([a for a, b in AB])
    sumB = 0
    ans = 0
    for a, b in AB:
        sumA -= a
        sumB += a + b
        ans += 1
        if sumB > sumA:
            break
    print(ans)

=======
Suggestion 2

def main():
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
        ans += a[i] * i + b[i] * (n - i)
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    c = []
    for i in range(n):
        c.append(a[i] + b[i])
    c.sort(reverse=True)
    sum = 0
    for i in range(0, n, 2):
        sum += c[i]
    print(sum)

=======
Suggestion 4

def solve():
    N = int(input())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N-1, -1, -1):
        A[i] += ans
        if A[i] < B[i]:
            ans += B[i] - A[i]
            A[i] = B[i]
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    a.sort(reverse=True)
    b.sort(reverse=True)
    a_sum = sum(a)
    b_sum = 0
    num = 0
    for i in range(n):
        a_sum -= a[i]
        b_sum += a[i] + b[i]
        num += 1
        if b_sum > a_sum:
            break
    print(num)
main()
#解答
#在每个镇上发表演讲的候选人都会获得该镇的所有选票。
#因此，高桥至少需要在具有最多支持高桥的选民的镇上发表演讲。
#因此，我们首先按照支持高桥的选民的数量对镇进行排序。
#然后，我们按照这个顺序依次发表演讲。
#在这种情况下，高桥将获得最多的选票。
#我们将在高桥获得的选票数超过青木获得的选票数时停止发表演讲。

=======
Suggestion 6

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # print(A)
    # print(B)
    sum = 0
    for i in range(N):
        sum += A[i]
    # print(sum)
    ave = sum / 2
    # print(ave)
    flag = False
    for i in range(N):
        sum -= A[i]
        if sum < ave:
            flag = True
            print(i + 1)
            break
    if flag == False:
        print(N)

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
    a.sort()
    b.sort()
    if n % 2 == 1:
        print(b[n//2] - a[n//2] + 1)
    else:
        print(b[n//2] + b[n//2-1] - a[n//2] - a[n//2-1] + 1)

=======
Suggestion 8

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int,input().split())
        a.append(ai)
        b.append(bi)

    a.sort(reverse=True)
    b.sort(reverse=True)
    cnt = 0
    i = 0
    j = 0
    while i < n and j < n:
        if a[i] > b[j]:
            cnt += 1
            i += 1
        j += 1

    print(cnt)

=======
Suggestion 9

def solve():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[0]+x[1], reverse=True)
    #print(AB)
    ans = 0
    for i in range(N):
        if i % 2 == 0:
            ans += AB[i][0]
        else:
            ans -= AB[i][1]
    print(ans)

=======
Suggestion 10

def solve():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        c, d = map(int, input().split())
        a.append(c)
        b.append(d)
    a.sort(reverse=True)
    b.sort(reverse=True)
    ans = 0
    for i in range(n):
        if a[i] > b[i]:
            ans += 1
    print(ans)
