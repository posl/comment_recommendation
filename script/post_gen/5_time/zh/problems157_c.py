Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    #print(N, M)
    s = []
    c = []
    for i in range(M):
        s_i, c_i = map(int, input().split())
        s.append(

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    s = []
    c = []
    for i in range(M):
        s_i, c_i = map(int, input().split())
        s.append(s_i)
        c.append(c_i)
    #print(N, M, s, c)
    for i in range(10**(N-1), 10**N):
        i_str = str(i)
        flag = True
        for j in range(M):
            if i_str[s[j]-1] != str(c[j]):
                flag = False
                break
        if flag:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 3

def main():
    N, M = [int(x) for x in input().split()]
    sc = []
    for i in range(M):
        sc.append([int(x) for x in input().split()])

    sc.sort(key=lambda x: x[0])
    if sc[0][0] == 1 and sc[0][1] == 0:
        print(-1)
        return

    num = [0] * N
    for i in range(M):
        num[sc[i][0] - 1] = sc[i][1]

    ans = 0
    for i in range(N):
        ans = ans * 10 + num[i]
    print(ans)

=======
Suggestion 4

def solve():
    n, m = map(int, input().split())
    s = [0] * m
    c = [0] * m
    for i in range(m):
        s[i], c[i] = map(int, input().split())
    ans = -1
    for i in range(10 ** n):
        i = str(i)
        if len(i) != n:
            continue
        for j in range(m):
            if i[s[j] - 1] != str(c[j]):
                break
        else:
            ans = i
            break
    print(ans)

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    s = []
    c = []
    for i in range(m):
        s1,c1 = map(int,input().split())
        s.append(s1)
        c.append(c1)

    if n == 1:
        print(c[0])
    elif n == 2:
        if s[0] == 1 and c[0] == 0:
            print(-1)
        else:
            print(c[0]*10+c[1])
    elif n == 3:
        if s[0] == 1 and c[0] == 0:
            if s[1] == 2 and c[1] == 0:
                print(-1)
            else:
                print(c[1]*100+c[2])
        elif s[0] == 1 and c[0] != 0:
            print(c[0]*100+c[1]*10+c[2])
        elif s[0] == 2 and c[0] == 0:
            if s[1] == 2 and c[1] == 0:
                print(-1)
            else:
                print(c[1]*10+c[2])
        elif s[0] == 2 and c[0] != 0:
            print(c[0]*10+c[1]*100+c[2])

=======
Suggestion 6

def check(n, m, s, c):
    if n > 3 or n < 1:
        print(-1)
        return
    if m > 5 or m < 0:
        print(-1)
        return
    if len(s) != m or len(c) != m:
        print(-1)
        return
    for i in range(m):
        if s[i] > n or s[i] < 1:
            print(-1)
            return
        if c[i] > 9 or c[i] < 0:
            print(-1)
            return
    if n == 1:
        print(c[0])
        return
    if n == 2:
        if s[0] == 1:
            print(c[0] * 10 + c[1])
            return
        else:
            print(c[1] * 10 + c[0])
            return
    if n == 3:
        if s[0] == 1:
            print(c[0] * 100 + c[1] * 10 + c[2])
            return
        elif s[0] == 2:
            print(c[1] * 100 + c[0] * 10 + c[2])
            return
        else:
            print(c[1] * 100 + c[2] * 10 + c[0])
            return

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    if n == 1:
        for i in range(m):
            s,c = map(int,input().split())
            if s == 1 and c == 0:
                print(0)
                return
            else:
                print(-1)
                return
    elif n == 2:
        for i in range(m):
            s,c = map(int,input().split())
            if s == 1 and c == 0:
                print(-1)
                return
            elif s == 2 and c == 0:
                print(-1)
                return
            elif s == 1 and c != 0:
                print(c*10)
                return
            elif s == 2 and c != 0:
                print(c)
                return
    elif n == 3:
        for i in range(m):
            s,c = map(int,input().split())
            if s == 1 and c == 0:
                print(-1)
                return
            elif s == 2 and c == 0:
                print(-1)
                return
            elif s == 3 and c == 0:
                print(-1)
                return
            elif s == 1 and c != 0:
                print(c*100)
                return
            elif s == 2 and c != 0:
                print(c*10)
                return
            elif s == 3 and c != 0:
                print(c)
                return

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    d = [10**i for i in range(n)]
    a = [0]*n
    for i in range(m):
        s,c = map(int,input().split())
        a[s-1] = c
    for i in range(10**n):
        t = i
        for j in range(n):
            if (t//d[j])%10 != a[j]:
                break
        else:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 9

def find_min(N, M, s, c):
    #print(N)
    #print(M)
    #print(s)
    #print(c)
    #print("")

    #check if there is a number with N digits
    if N == 1:
        return c[0]
    if N == 2:
        if M == 1:
            if s[0] == 1:
                return c[0] * 10
            elif s[0] == 2:
                return c[0] + c[1] * 10
            else:
                return c[0]
        elif M == 2:
            if s[0] == 1:
                return c[0] * 10 + c[1]
            elif s[0] == 2:
                return c[1] * 10 + c[0]
            else:
                return c[0] * 10 + c[1]
        else:
            return -1
    if N == 3:
        if M == 1:
            if s[0] == 1:
                return c[0] * 100
            elif s[0] == 2:
                return c[0] * 10 + c[1] * 100
            elif s[0] == 3:
                return c[0] + c[1] * 10 + c[2] * 100
            else:
                return c[0]
        elif M == 2:
            if s[0] == 1:
                return c[0] * 100 + c[1]
            elif s[0] == 2:
                return c[1] * 100 + c[0] * 10
            elif s[0] == 3:
                return c[2] * 100 + c[0] + c[1] * 10
            else:
                return c[0] * 100 + c[1]
        elif M == 3:
            if s[0] == 1:
                return c[0] * 100 + c[1] * 10 + c[2]
            elif s[0] == 2:
                return c[1] * 100 + c[0] + c[2] * 10
            elif s[0] ==

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    for i in range(m):
        s, c = map(int, input().split())
        print(s, c)
