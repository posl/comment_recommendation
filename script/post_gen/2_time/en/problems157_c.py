Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    S = [0] * M
    C = [0] * M
    for i in range(M):
        S[i], C[i] = map(int, input().split())
    for i in range(1000):
        s = str(i)
        if len(s) != N:
            continue
        ok = True
        for j in range(M):
            if s[S[j] - 1] != str(C[j]):
                ok = False
                break
        if ok:
            print(s)
            return
    print(-1)

main()

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    S = [0] * M
    C = [0] * M
    for i in range(M):
        S[i], C[i] = map(int, input().split())
    if N == 1:
        if M == 0:
            print(0)
        else:
            if S[0] == 1:
                print(C[0])
            else:
                print(-1)
    else:
        if N == 2:
            for i in range(10):
                for j in range(10):
                    if (i * 10 + j) % (10 ** (N - S[0])) == C[0] * (10 ** (N - S[0])):
                        if M == 1:
                            print(i * 10 + j)
                        else:
                            for k in range(1, M):
                                if (i * 10 + j) % (10 ** (N - S[k])) == C[k] * (10 ** (N - S[k])):
                                    if k == M - 1:
                                        print(i * 10 + j)
                                else:
                                    break
        else:
            if N == 3:
                for i in range(10):
                    for j in range(10):
                        for k in range(10):
                            if (i * 100 + j * 10 + k) % (10 ** (N - S[0])) == C[0] * (10 ** (N - S[0])):
                                if M == 1:
                                    print(i * 100 + j * 10 + k)
                                else:
                                    for l in range(1, M):
                                        if (i * 100 + j * 10 + k) % (10 ** (N - S[l])) == C[l] * (10 ** (N - S[l])):
                                            if l == M - 1:
                                                print(i * 100 + j * 10 + k)
                                        else:
                                            break
            else:
                print(-1)

main()

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    s = [0] * m
    c = [0] * m
    for i in range(m):
        s[i], c[i] = map(int, input().split())
    if n == 1:
        if m == 0:
            print(0)
        elif m == 1:
            print(c[0])
        else:
            print(-1)
    elif n == 2:
        if m == 0:
            print(10, 11)
        elif m == 1:
            if s[0] == 1:
                print(c[0] * 10, c[0] * 10 + 1)
            else:
                print(c[0], c[0] + 10)
        elif m == 2:
            if s[0] == 1:
                if s[1] == 2:
                    print(c[0] * 10 + c[1])
                else:
                    print(-1)
            else:
                if s[1] == 1:
                    print(c[1] * 10 + c[0])
                else:
                    print(-1)
        else:
            print(-1)
    else:
        if m == 0:
            print(100, 101)
        elif m == 1:
            if s[0] == 1:
                print(c[0] * 100 + 10, c[0] * 100 + 11)
            elif s[0] == 2:
                print(c[0] * 10 + 10, c[0] * 10 + 11)
            else:
                print(c[0] + 100, c[0] + 101)
        elif m == 2:
            if s[0] == 1:
                if s[1] == 2:
                    print(c[0] * 100 + c[1] * 10)
                elif s[1] == 3:
                    print(c[0] * 100 + c[1])
                else:
                    print(-1)
            elif s[0] == 2:
                if s[1] == 1:
                    print(c[1] * 100 + c[0] * 10)
                elif s[1] ==

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    s = [0]*m
    c = [0]*m
    for i in range(m):
        s[i], c[i] = map(int, input().split())
    for i in range(10**(n-1), 10**n):
        if len(set(str(i))) != len(str(i)):
            continue
        for j in range(m):
            if int(str(i)[s[j]-1]) != c[j]:
                break
        else:
            print(i)
            return
    print(-1)

=======
Suggestion 5

def get_input():
    N, M = map(int, input().split())
    s = []
    c = []
    for i in range(M):
        s_i, c_i = map(int, input().split())
        s.append(s_i)
        c.append(c_i)
    return N, M, s, c

=======
Suggestion 6

def main():

    N, M = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(M)]

    if N == 1:
        for s, c in sc:
            if s == 1 and c == 0:
                print(-1)
                return
        print(0)
        return

    for i in range(1000):
        if len(str(i)) == N:
            for s, c in sc:
                if str(i)[s-1] != str(c):
                    break
            else:
                print(i)
                return

    print(-1)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    sc = [input().split() for _ in range(m)]
    ans = -1
    for i in range(1000):
        if len(str(i)) == n:
            for s, c in sc:
                if str(i)[int(s) - 1] != c:
                    break
            else:
                ans = i
                break
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(M)]
    S.sort(key=lambda x: x[0])
    if N == 1:
        if M == 0:
            print(0)
            return
        else:
            for s, c in S:
                if s == 1 and c == 0:
                    print(-1)
                    return
                else:
                    print(c)
                    return
    else:
        if M == 0:
            print(10**(N-1))
            return
        else:
            if S[0][0] == 1:
                if S[0][1] == 0:
                    print(-1)
                    return
                else:
                    if M == 1:
                        print(S[0][1]*10**(N-1))
                        return
                    else:
                        if S[1][0] == 2:
                            print(S[0][1]*10**(N-1)+S[1][1])
                            return
                        else:
                            print(S[0][1]*10**(N-1)+10**(N-2))
                            return
            else:
                print(S[0][1]*10**(N-1)+10**(N-2))
                return

=======
Suggestion 9

def get_num(N, M, s, c):
    if M == 0:
        if N == 1:
            return 0
        else:
            return -1
    if N == 1:
        if M == 1 and s[0] == 1:
            return c[0]
        else:
            return -1
    if N == 2:
        if M == 1 and s[0] == 1:
            return c[0] * 10
        elif M == 1 and s[0] == 2:
            return c[0]
        else:
            return -1
    if N == 3:
        if M == 1 and s[0] == 1:
            return c[0] * 100
        elif M == 1 and s[0] == 2:
            return c[0] * 10
        elif M == 1 and s[0] == 3:
            return c[0]
        elif M == 2 and s[0] == 1 and s[1] == 2:
            return c[0] * 10 + c[1]
        elif M == 2 and s[0] == 1 and s[1] == 3:
            return c[0] * 100 + c[1] * 10
        elif M == 2 and s[0] == 2 and s[1] == 3:
            return c[0] * 10 + c[1]
        else:
            return -1

=======
Suggestion 10

def check(n, s, c):
    if n[s] == c:
        return True
    else:
        return False
