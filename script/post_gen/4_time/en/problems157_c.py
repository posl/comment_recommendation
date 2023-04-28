Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    s = [0] * m
    c = [0] * m
    for i in range(m):
        s[i], c[i] = map(int, input().split())
    for i in range(10 ** (n - 1), 10 ** n):
        flag = True
        for j in range(m):
            if int(str(i)[s[j] - 1]) != c[j]:
                flag = False
        if flag:
            print(i)
            return
    print(-1)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    s = [0] * M
    c = [0] * M
    for i in range(M):
        s[i], c[i] = map(int, input().split())
    for i in range(10**(N-1), 10**N):
        i = str(i)
        for j in range(M):
            if int(i[s[j]-1]) != c[j]:
                break
        else:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    s = [0] * M
    c = [0] * M
    for i in range(M):
        s[i], c[i] = map(int, input().split())
    for i in range(10 ** N):
        i = str(i)
        if len(i) == N:
            for j in range(M):
                if i[s[j] - 1] != str(c[j]):
                    break
            else:
                print(i)
                exit()
    print(-1)
main()

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    s = [0] * M
    c = [0] * M
    for i in range(M):
        s[i], c[i] = map(int, input().split())
    #print(N,M,s,c)
    for i in range(10**(N-1), 10**N):
        #print(i)
        flag = True
        for j in range(M):
            if int(str(i)[s[j]-1]) != c[j]:
                flag = False
                break
        if flag:
            print(i)
            return
    print(-1)
    return

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    s = []
    c = []
    for i in range(m):
        a, b = map(int, input().split())
        s.append(a)
        c.append(b)

    for i in range(10**(n-1), 10**n):
        ii = str(i)
        flag = True
        for j in range(m):
            if ii[s[j]-1] != str(c[j]):
                flag = False
        if flag:
            print(i)
            return
    print(-1)

=======
Suggestion 6

def main():
    n,m = map(int, input().split())
    s = [0] * m
    c = [0] * m
    for i in range(m):
        s[i], c[i] = map(int, input().split())
    for i in range(10 ** n):
        sflg = True
        for j in range(m):
            if int(str(i)[s[j] - 1]) != c[j]:
                sflg = False
                break
        if sflg:
            print(i)
            return
    print(-1)
    return

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(M)]

    if N == 1:
        if M == 0:
            print(0)
        else:
            for i in range(10):
                if [1, i] in sc:
                    print(i)
                    exit()
            print(-1)
    elif N == 2:
        if M == 0:
            print(10)
        else:
            for i in range(10):
                for j in range(10):
                    if [1, i] in sc and [2, j] in sc:
                        print(i*10+j)
                        exit()
            print(-1)
    else:
        if M == 0:
            print(100)
        else:
            for i in range(10):
                for j in range(10):
                    for k in range(10):
                        if [1, i] in sc and [2, j] in sc and [3, k] in sc:
                            print(i*100+j*10+k)
                            exit()
            print(-1)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(m)]
    ans = [-1 for _ in range(n)]
    for s, c in sc:
        if ans[s-1] == -1 or ans[s-1] == c:
            ans[s-1] = c
        else:
            print(-1)
            return
    if ans[0] == 0 and n > 1:
        print(-1)
        return
    if ans[0] == -1:
        ans[0] = 1
    print(''.join(map(str, ans)))

=======
Suggestion 9

def solve():
    N, M = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(M)]
    for i in range(10 ** N):
        s = str(i)
        if len(s) != N:
            continue
        for j, c in sc:
            if int(s[j - 1]) != c:
                break
        else:
            return s
    return -1

print(solve())

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(m)]
    sc.sort()
    if n == 1:
        if m == 0:
            print(0)
        elif m == 1:
            print(sc[0][1])
        else:
            print(-1)
    elif n == 2:
        if m == 0:
            print(10)
        elif m == 1:
            print(sc[0][1] * 10)
        elif m == 2:
            if sc[0][0] == 1:
                print(sc[0][1] * 10 + sc[1][1])
            else:
                print(sc[0][1] + sc[1][1] * 10)
        else:
            print(-1)
    elif n == 3:
        if m == 0:
            print(100)
        elif m == 1:
            print(sc[0][1] * 100)
        elif m == 2:
            if sc[0][0] == 1:
                print(sc[0][1] * 100 + sc[1][1] * 10)
            elif sc[0][0] == 2:
                print(sc[0][1] * 100 + sc[1][1])
            else:
                print(-1)
        elif m == 3:
            if sc[0][0] == 1 and sc[1][0] == 2:
                print(sc[0][1] * 100 + sc[1][1] * 10 + sc[2][1])
            else:
                print(-1)
        else:
            print(-1)
    else:
        print(-1)
