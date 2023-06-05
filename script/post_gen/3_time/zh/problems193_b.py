Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    t = []
    for i in range(n):
        a, p, x = map(int, input().split())
        t.append([a, p, x])
    t.sort()
    for i in range(n):
        if t[i][2] > 0:
            print(t[i][1])
            return
    print(-1)
    return

=======
Suggestion 2

def solve():
    n = int(input())
    a = []
    p = []
    x = []
    for i in range(n):
        a1,p1,x1 = map(int,input().split())
        a.append(a1)
        p.append(p1)
        x.append(x1)
    for i in range(n):
        for j in range(i+1,n):
            if a[i] > a[j]:
                a[i],a[j] = a[j],a[i]
                p[i],p[j] = p[j],p[i]
                x[i],x[j] = x[j],x[i]
    for i in range(n):
        if x[i] > 0:
            print(p[i])
            return
    print(-1)
    return

=======
Suggestion 3

def solve():
    n = int(input())
    apx = [list(map(int, input().split())) for _ in range(n)]
    apx.sort()
    for a, p, x in apx:
        if x > 0:
            print(p)
            break
    else:
        print(-1)

solve()

=======
Suggestion 4

def solve():
    N = int(input())
    APX = [list(map(int, input().split())) for _ in range(N)]
    APX.sort(key=lambda x: x[0])
    print(APX)
    for i in range(N):
        if APX[i][2] > 0:
            print(APX[i][1])
            return
    print(-1)

=======
Suggestion 5

def buy_snuke():
    n = int(input())
    a_list = []
    p_list = []
    x_list = []
    for i in range(n):
        a, p, x = map(int, input().split())
        a_list.append(a)
        p_list.append(p)
        x_list.append(x)
    min_p = 10**9
    for i in range(n):
        if x_list[i] > 0:
            if p_list[i] < min_p:
                min_p = p_list[i]
    if min_p == 10**9:
        return -1
    else:
        return min_p

print(buy_snuke())

=======
Suggestion 6

def get_min_money(n, stores):
    min_money = -1

    for i in range(n):
        if stores[i][2] > 0:
            if min_money == -1 or min_money > stores[i][1]:
                min_money = stores[i][1]

    return min_money

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    p = []
    x = []
    for i in range(n):
        a_i, p_i, x_i = map(int, input().split())
        a.append(a_i)
        p.append(p_i)
        x.append(x_i)
    min_p = 1000000000
    for i in range(n):
        if x[i] > 0:
            min_p = min(min_p, p[i])
    if min_p == 1000000000:
        print(-1)
        return
    print(min_p)

=======
Suggestion 8

def readinput():
    n=int(input())
    shops=[]
    for i in range(n):
        a,p,x=map(int,input().split())
        shops.append((a,p,x))
    return n,shops

=======
Suggestion 9

def problem193_b():
    pass

=======
Suggestion 10

def get_input():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        a,p,x = map(int,input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    return N,A,P,X
