Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    S = [0] * M
    C = [0] * M
    for i in range(M):
        S[i], C[i] = map(int, input().split())

    if N == 1:
        if M == 0:
            print(0)
        elif M == 1:
            print(C[0])
        else:
            print(-1)
    elif N == 2:
        if M == 0:
            print(10, 99)
        elif M == 1:
            if S[0] == 1:
                print(C[0] * 10, C[0] * 10 + 9)
            else:
                print(10 + C[0], 19 + C[0])
        elif M == 2:
            if S[0] == 1 and S[1] == 2:
                print(C[0] * 10 + C[1], C[0] * 10 + C[1])
            else:
                print(-1)
        else:
            print(-1)
    else:  # N == 3
        if M == 0:
            print(100, 999)
        elif M == 1:
            if S[0] == 1:
                print(C[0] * 100, C[0] * 100 + 99)
            elif S[0] == 2:
                print(100 + C[0] * 10, 199 + C[0] * 10)
            else:
                print(100 + C[0], 199 + C[0])
        elif M == 2:
            if S[0] == 1 and S[1] == 2:
                print(C[0] * 100 + C[1] * 10, C[0] * 100 + C[1] * 10 + 9)
            elif S[0] == 1 and S[1] == 3:
                print(C[0] * 100 + C[1], C[0] * 100 + C[1] + 9)
            elif S[0] == 2 and S[1] == 3:
                print(100 + C[0] * 10 + C[1

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    S = [0] * M
    C = [0] * M
    for i in range(M):
        S[i], C[i] = map(int, input().split())
        S[i] -= 1 # 0-indexed

    if N == 1:
        if M == 0:
            print(0)
        else:
            print(C[0])
        return

    if M == 0:
        print(10**(N-1))
        return

    ans = [-1] * N
    for i in range(M):
        if ans[S[i]] == -1:
            ans[S[i]] = C[i]
        elif ans[S[i]] != C[i]:
            print(-1)
            return

    if ans[0] == 0:
        print(-1)
        return

    if ans[0] == -1:
        ans[0] = 1

    for i in range(N):
        if ans[i] == -1:
            ans[i] = 0

    print(''.join(map(str, ans)))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    if M == 0:
        if N == 1:
            print(0)
        else:
            print(10 ** (N - 1))
        return
    s = [0] * (N + 1)
    c = [0] * (N + 1)
    for i in range(M):
        s[i], c[i] = map(int, input().split())
    if N == 1:
        if M == 1 and s[0] == 1:
            print(c[0])
        else:
            print(-1)
        return
    if M == 1:
        if s[0] == 1:
            if c[0] == 0:
                print(-1)
                return
            else:
                print(str(c[0]) + '0' * (N - 1))
                return
        else:
            print(str(c[0]) + '0' * (N - 2) + '1')
            return
    for i in range(M):
        if s[i] == 1 and c[i] == 0:
            print(-1)
            return
    for i in range(M):
        if s[i] == 1:
            print(str(c[i]) + '0' * (N - 1), end='')
            return
    print(-1)
    return

main()

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    if N == 1:
        if M == 0:
            print(0)
            return
        else:
            s, c = map(int, input().split())
            if s == 1 and c == 0:
                print(-1)
            else:
                print(c)
            return
    else:
        s = []
        c = []
        for _ in range(M):
            s_i, c_i = map(int, input().split())
            s.append(s_i)
            c.append(c_i)
        ans = [0] * N
        for i in range(N):
            ans[i] = 1
        for i in range(M):
            ans[s[i] - 1] = c[i]
        if ans[0] == 1:
            ans[0] = 2
        print("".join(map(str, ans)))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(M)]
    for i in range(1000):
        if len(str(i)) == N:
            for j in sc:
                if str(i)[j[0]-1] != str(j[1]):
                    break
            else:
                print(i)
                return
    print(-1)

=======
Suggestion 6

def check(n, M, S, C):
    for i in range(M):
        if n[S[i]-1] != str(C[i]):
            return False
    return True

N, M = map(int, input().split())
S = []
C = []
for i in range(M):
    s, c = map(int, input().split())
    S.append(s)
    C.append(c)

for i in range(10**N):
    n = str(i)
    if len(n) != N:
        n = '0'*(N-len(n)) + n
    if check(n, M, S, C):
        print(n)
        exit()
print(-1)

=======
Suggestion 7

def check(n, s, c):
    return str(n)[s - 1] == str(c)

n, m = map(int, input().split())
s = [0] * m
c = [0] * m
for i in range(m):
    s[i], c[i] = map(int, input().split())

=======
Suggestion 8

def check(n, s, c):
    for i in range(len(s)):
        if n[s[i] - 1] != c[i]:
            return False
    return True

=======
Suggestion 9

def check(n, s, c):
    if n[s] == c:
        return True
    else:
        return False

n, m = map(int, input().split())
s = [0] * m
c = [0] * m
for i in range(m):
    s[i], c[i] = map(int, input().split())

=======
Suggestion 10

def check(n, s, c):
    return int(str(n)[s-1]) == c
