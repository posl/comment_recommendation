Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    s = [0] * M
    c = [0] * M
    for i in range(M):
        s[i], c[i] = map(int, input().split())
    if N == 1:
        if M == 0:
            print(0)
        else:
            if s[0] == 1:
                print(c[0])
            else:
                print(-1)
    elif N == 2:
        if M == 0:
            print(10, 11)
        elif M == 1:
            if s[0] == 1:
                if c[0] == 0:
                    print(10)
                else:
                    print(10 * c[0] + 1, 10 * c[0] + 10 + 1)
            else:
                print(-1)
        else:
            if s[0] == 1:
                if c[0] == 0:
                    if s[1] == 2:
                        print(10 * c[1] + 10)
                    else:
                        print(-1)
                else:
                    if s[1] == 2:
                        print(10 * c[0] + 10 * c[1] + 10)
                    else:
                        print(-1)
            else:
                print(-1)
    else:
        if M == 0:
            print(100, 101, 110, 111)
        elif M == 1:
            if s[0] == 1:
                if c[0] == 0:
                    print(100, 101, 110, 111)
                else:
                    print(100 * c[0] + 10, 100 * c[0] + 10 + 1, 100 * c[0] + 10 + 10, 100 * c[0] + 10 + 10 + 1)
            elif s[0] == 2:
                print(100 + 10 * c[0], 100 + 10 * c[0] + 1, 100 + 10 * c[0] + 10, 100 + 10 * c[0] + 10 + 1)
            elif s[0] == 3:

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    s = [0] * M
    c = [0] * M
    for i in range(M):
        s[i], c[i] = map(int, input().split())
    if M == 0:
        if N == 1:
            print(0)
        else:
            print(10 ** (N - 1))
        return
    else:
        for i in range(10 ** (N - 1), 10 ** N):
            for j in range(M):
                if i // 10 ** (N - s[j]) % 10 == c[j]:
                    if j == M - 1:
                        print(i)
                        return
                else:
                    break
    print(-1)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    S = []
    C = []
    for i in range(M):
        s, c = map(int, input().split())
        S.append(s)
        C.append(c)
    if M == 0:
        if N == 1:
            print(0)
        else:
            print(10 ** (N - 1))
    else:
        for i in range(10 ** (N - 1), 10 ** N):
            for j in range(M):
                if int(str(i)[S[j] - 1]) != C[j]:
                    break
            else:
                print(i)
                break
        else:
            print(-1)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    s = []
    c = []
    for i in range(m):
        s_i, c_i = map(int, input().split())
        s.append(s_i)
        c.append(c_i)
    if n == 1:
        if m == 0:
            print(0)
        else:
            if s[0] == 1:
                print(c[0])
            else:
                print(-1)
    elif n == 2:
        if m == 0:
            print(10)
        elif m == 1:
            if s[0] == 1:
                print(c[0] * 10)
            else:
                print(-1)
        else:
            if s[0] == 1 and s[1] == 2:
                if c[0] == c[1]:
                    print(c[0] * 10 + c[1])
                else:
                    print(-1)
            else:
                print(-1)
    else:
        if m == 0:
            print(100)
        elif m == 1:
            if s[0] == 1:
                print(c[0] * 100)
            elif s[0] == 2:
                print(c[0] * 10 + 0)
            else:
                print(-1)
        elif m == 2:
            if s[0] == 1 and s[1] == 2:
                if c[0] == c[1]:
                    print(c[0] * 100 + c[1] * 10)
                else:
                    print(-1)
            elif s[0] == 1 and s[1] == 3:
                if c[0] == c[1]:
                    print(c[0] * 100 + c[1])
                else:
                    print(-1)
            elif s[0] == 2 and s[1] == 3:
                if c[0] == c[1]:
                    print(c[0] * 10 + c[1])
                else:
                    print(-1)
            else:
                print(-1)
        else:
            if s[0] == 1 and s[1] == 2 and s[2] == 3:
                if c[0] == c[

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    s = []
    c = []
    for _ in range(M):
        s_, c_ = map(int, input().split())
        s.append(s_)
        c.append(c_)
    if N == 1 and M == 0:
        print(0)
        return
    if M == 0:
        print(10**(N-1))
        return
    if N > 1:
        if 1 not in s:
            s.append(1)
            c.append(1)
    for i in range(10**(N-1), 10**N):
        for j in range(M):
            if int(str(i)[s[j]-1]) != c[j]:
                break
        else:
            print(i)
            return
    print(-1)
    return

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    s = []
    c = []
    for i in range(M):
        s_i,c_i = map(int,input().split())
        s.append(s_i)
        c.append(c_i)
    #print(s)
    #print(c)
    if N == 1:
        if M == 0:
            print(0)
        else:
            if s[0] == 1:
                print(c[0])
            else:
                print(-1)
    elif N == 2:
        if M == 0:
            print(10,99)
        elif M == 1:
            if s[0] == 1:
                print(10*c[0]+0,10*c[0]+9)
            elif s[0] == 2:
                print(10+10*c[0],99+10*c[0])
            else:
                print(-1)
        else:
            if s[0] == 1 and s[1] == 2:
                if c[0] == c[1]:
                    print(10*c[0]+c[1])
                else:
                    print(-1)
            else:
                print(-1)
    else:
        if M == 0:
            print(100,999)
        elif M == 1:
            if s[0] == 1:
                print(100*c[0]+0,100*c[0]+99)
            elif s[0] == 2:
                print(100+10*c[0],999+10*c[0])
            elif s[0] == 3:
                print(100+100*c[0],999+100*c[0])
            else:
                print(-1)
        elif M == 2:
            if s[0] == 1 and s[1] == 2:
                if c[0] == c[1]:
                    print(100*c[0]+c[1])
                else:
                    print(-1)
            elif s[0] == 1 and s[1] == 3:
                if c[0] == c[1]:
                    print(100*c[0]+10*c[1])
                else:
                    print(-1)
            elif s[0] == 2 and s[1] == 3:
                if c[0]

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    d = {}
    for i in range(m):
        s, c = map(int, input().split())
        if s in d:
            if d[s] != c:
                print(-1)
                return
        else:
            d[s] = c
    if 1 in d and d[1] == 0:
        print(-1)
        return
    for i in range(1, n+1):
        if i in d:
            print(d[i], end="")
        else:
            if i == 1:
                print(1, end="")
            else:
                print(0, end="")
    print()

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    if N == 1 and M == 0:
        print(0)
        return
    if M == 0:
        print(10**(N-1))
        return
    s_c = []
    for i in range(M):
        s, c = map(int, input().split())
        s_c.append([s, c])
    s_c.sort()
    for i in range(M):
        if i == 0:
            if s_c[i][0] == 1 and s_c[i][1] == 0:
                print(-1)
                return
            else:
                num = s_c[i][1]
        else:
            if s_c[i][0] == s_c[i-1][0]:
                print(-1)
                return
            else:
                num += s_c[i][1] * 10**(s_c[i][0]-1)
    if len(str(num)) != N:
        print(-1)
        return
    print(num)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    s_c = [list(map(int, input().split())) for _ in range(M)]

    if N == 1:
        if M == 0:
            print(0)
        else:
            if s_c[0][1] == 0:
                print(-1)
            else:
                print(s_c[0][1])
    else:
        if M == 0:
            print(10 ** (N - 1))
        else:
            if N == 2:
                if s_c[0][0] == 1:
                    if s_c[0][1] == 0:
                        print(-1)
                    else:
                        print(10 * s_c[0][1])
                else:
                    print(s_c[0][1] * 10 + 10 ** (N - 1))
            else:
                if s_c[0][0] == 1:
                    if s_c[0][1] == 0:
                        print(-1)
                    else:
                        print(100 * s_c[0][1] + 10 ** (N - 1))
                elif s_c[0][0] == 2:
                    if s_c[0][1] == 0:
                        print(-1)
                    else:
                        print(10 * s_c[0][1] + 10 ** (N - 1))
                else:
                    print(s_c[0][1] * 100 + 10 ** (N - 1))
