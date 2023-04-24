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
            else:
                ans += S
        else:
            if T[i] == T[i-K]:
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
            if T[i] == 'r' and T[i-K] != 'p':
                ans += P
            elif T[i] == 's' and T[i-K] != 'r':
                ans += R
            elif T[i] == 'p' and T[i-K] != 's':
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
        if i >= K:
            if T[i] == T[i-K]:
                T = T[:i] + 'x' + T[i+1:]
        if T[i] == 'r':
            ans += P
        elif T[i] == 's':
            ans += R
        elif T[i] == 'p':
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
            T = T[:i] + 'X' + T[i+1:]
        else:
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
Suggestion 6

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = list(input())
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
            if T[i] == T[i-K]:
                if i+K < N:
                    if T[i] == 'r' and T[i+K] != 'p':
                        T[i] = 'p'
                        ans += P
                    elif T[i] == 's' and T[i+K] != 'r':
                        T[i] = 'r'
                        ans += R
                    elif T[i] == 'p' and T[i+K] != 's':
                        T[i] = 's'
                        ans += S
                else:
                    if T[i] == 'r':
                        T[i] = 'p'
                        ans += P
                    elif T[i] == 's':
                        T[i] = 'r'
                        ans += R
                    elif T[i] == 'p':
                        T[i] = 's'
                        ans += S
            else:
                if T[i] == 'r':
                    ans += P
                elif T[i] == 's':
                    ans += R
                else:
                    ans += S
    print(ans)

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()
    ans = 0
    for i in range(n):
        if i < k:
            if t[i] == "r":
                ans += p
            elif t[i] == "s":
                ans += r
            else:
                ans += s
        else:
            if t[i] == "r" and t[i-k] != "p":
                ans += p
                t = t[:i] + "p" + t[i+1:]
            elif t[i] == "s" and t[i-k] != "r":
                ans += r
                t = t[:i] + "r" + t[i+1:]
            elif t[i] == "p" and t[i-k] != "s":
                ans += s
                t = t[:i] + "s" + t[i+1:]
    print(ans)

=======
Suggestion 8

def main():
    N,K = map(int,input().split())
    R,S,P = map(int,input().split())
    T = input()
    ans = 0
    for i in range(N):
        if i >= K:
            if T[i] == T[i-K]:
                T = T[:i] + 'x' + T[i+1:]
    for i in range(N):
        if T[i] == 'r':
            ans += P
        elif T[i] == 's':
            ans += R
        elif T[i] == 'p':
            ans += S
    print(ans)

main()

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()

    score = 0
    for i in range(N):
        if i >= K and T[i] == T[i-K]:
            T = T[:i] + 'x' + T[i+1:]
        else:
            if T[i] == 'r':
                score += P
            elif T[i] == 's':
                score += R
            elif T[i] == 'p':
                score += S

    print(score)

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()
    ans = 0
    for i in range(k):
        if t[i] == 'r':
            ans += p
        elif t[i] == 's':
            ans += r
        else:
            ans += s
    for i in range(k,n):
        if t[i] == t[i-k]:
            t = t[:i] + 'x' + t[i+1:]
        else:
            if t[i] == 'r':
                ans += p
            elif t[i] == 's':
                ans += r
            else:
                ans += s
    print(ans)
