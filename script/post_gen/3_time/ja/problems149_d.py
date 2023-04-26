Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    ans = 0
    for i in range(N):
        if i < K:
            if T[i] == 'r':
                ans += P
            elif T[i] == 's':
                ans += R
            elif T[i] == 'p':
                ans += S
        else:
            if T[i] == T[i-K]:
                T = T[:i] + 'x' + T[i+1:]
            else:
                if T[i] == 'r':
                    ans += P
                elif T[i] == 's':
                    ans += R
                elif T[i] == 'p':
                    ans += S
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    ans = 0
    for i in range(N):
        if i < K:
            if T[i] == 'r':
                ans += P
            elif T[i] == 's':
                ans += R
            elif T[i] == 'p':
                ans += S
        else:
            if T[i] == 'r':
                if T[i-K] == 'r':
                    T = T[:i] + 'x' + T[i+1:]
                else:
                    ans += P
            elif T[i] == 's':
                if T[i-K] == 's':
                    T = T[:i] + 'x' + T[i+1:]
                else:
                    ans += R
            elif T[i] == 'p':
                if T[i-K] == 'p':
                    T = T[:i] + 'x' + T[i+1:]
                else:
                    ans += S
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    ans = 0
    for i in range(N):
        if i < K:
            if T[i] == 'r':
                ans += P
            elif T[i] == 's':
                ans += R
            else:
                ans += S
        else:
            if T[i] == 'r' and T[i-K] != 'p':
                ans += P
            elif T[i] == 's' and T[i-K] != 'r':
                ans += R
            elif T[i] == 'p' and T[i-K] != 's':
                ans += S
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    ans = 0
    for i in range(N):
        if i >= K and T[i] == T[i-K]:
            T = T[:i] + 'x' + T[i+1:]
    for i in range(N):
        if T[i] == 'r':
            ans += P
        elif T[i] == 's':
            ans += R
        elif T[i] == 'p':
            ans += S
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    ans = 0
    for i in range(N):
        if i >= K and T[i] == T[i-K]:
            T = T[:i] + 'x' + T[i+1:]
        else:
            if T[i] == 'r':
                ans += P
            elif T[i] == 's':
                ans += R
            else:
                ans += S
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    ans = 0
    for i in range(n):
        if i < k:
            if t[i] == "r":
                ans += p
            elif t[i] == "s":
                ans += r
            elif t[i] == "p":
                ans += s
        else:
            if t[i] == "r" and t[i-k] != "p":
                ans += p
            elif t[i] == "s" and t[i-k] != "r":
                ans += r
            elif t[i] == "p" and t[i-k] != "s":
                ans += s
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    
    ans = 0
    for i in range(N):
        if i >= K and T[i] == T[i-K]:
            T = T[:i] + "x" + T[i+1:]
        else:
            if T[i] == "r":
                ans += P
            elif T[i] == "s":
                ans += R
            elif T[i] == "p":
                ans += S
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    ans = 0
    for i in range(N):
        if T[i] == 'r':
            ans += P
        elif T[i] == 's':
            ans += R
        elif T[i] == 'p':
            ans += S
    for i in range(N-K):
        if T[i] == T[i+K]:
            if T[i] == 'r':
                ans -= P
            elif T[i] == 's':
                ans -= R
            elif T[i] == 'p':
                ans -= S
    print(ans)

=======
Suggestion 9

def main():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()
    ans = 0
    for i in range(n):
        if i < k:
            if t[i] == 'r':
                ans += p
            elif t[i] == 's':
                ans += r
            else:
                ans += s
        else:
            if t[i] == 'r' and t[i-k] != 'r':
                ans += p
            elif t[i] == 's' and t[i-k] != 's':
                ans += r
            elif t[i] == 'p' and t[i-k] != 'p':
                ans += s
    print(ans)

=======
Suggestion 10

def main():
    N,K = map(int,input().split())
    R,S,P = map(int,input().split())
    T = input()
    ans = 0
    for i in range(N):
        if i < K:
            if T[i] == "r":
                ans += P
            elif T[i] == "s":
                ans += R
            else:
                ans += S
        else:
            if T[i] == "r":
                if T[i-K] == "r":
                    T = T[:i] + "x" + T[i+1:]
                else:
                    ans += P
            elif T[i] == "s":
                if T[i-K] == "s":
                    T = T[:i] + "x" + T[i+1:]
                else:
                    ans += R
            else:
                if T[i-K] == "p":
                    T = T[:i] + "x" + T[i+1:]
                else:
                    ans += S
    print(ans)
