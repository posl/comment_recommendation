Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    ans = 0
    for i in range(K):
        ans += R if T[i] == 's' else S if T[i] == 'p' else P if T[i] == 'r' else 0
        if i + K < N and T[i] == T[i + K]:
            T = T[:i + K] + 'x' + T[i + K + 1:]
    for i in range(K, N):
        ans += R if T[i] == 's' else S if T[i] == 'p' else P if T[i] == 'r' else 0
    print(ans)

=======
Suggestion 2

def input_to_int():
    return [int(x) for x in input().split()]

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    score = 0
    for i in range(N):
        if i < K:
            if T[i] == 'r':
                score += P
            elif T[i] == 's':
                score += R
            else:
                score += S
        else:
            if T[i] == 'r':
                if T[i-K] == 'r':
                    T[i] = 'x'
                else:
                    score += P
            elif T[i] == 's':
                if T[i-K] == 's':
                    T[i] = 'x'
                else:
                    score += R
            else:
                if T[i-K] == 'p':
                    T[i] = 'x'
                else:
                    score += S
    print(score)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    score = 0
    for i in range(N):
        if i < K:
            if T[i] == "r":
                score += P
            elif T[i] == "s":
                score += R
            elif T[i] == "p":
                score += S
        else:
            if T[i] == "r":
                if T[i-K] == "r":
                    T = T[:i] + "x" + T[i+1:]
                else:
                    score += P
            elif T[i] == "s":
                if T[i-K] == "s":
                    T = T[:i] + "x" + T[i+1:]
                else:
                    score += R
            elif T[i] == "p":
                if T[i-K] == "p":
                    T = T[:i] + "x" + T[i+1:]
                else:
                    score += S
    print(score)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    ans = 0
    for i in range(n):
        if i >= k and t[i] == t[i - k] and t[i - k] != 'x':
            t = t[:i] + 'x' + t[i + 1:]
        else:
            if t[i] == 'r':
                ans += p
            elif t[i] == 's':
                ans += r
            else:
                ans += s
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
            else:
                ans += s
        else:
            if t[i] == "r":
                if t[i-k] == "r":
                    t = t[:i] + "x" + t[i+1:]
                else:
                    ans += p
            elif t[i] == "s":
                if t[i-k] == "s":
                    t = t[:i] + "x" + t[i+1:]
                else:
                    ans += r
            else:
                if t[i-k] == "p":
                    t = t[:i] + "x" + t[i+1:]
                else:
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
        if i < K:
            if T[i] == 'r':
                ans += P
            elif T[i] == 's':
                ans += R
            else:
                ans += S
        else:
            if T[i] == T[i-K]:
                T[i] = 'x'
            else:
                if T[i] == 'r':
                    ans += P
                elif T[i] == 's':
                    ans += R
                else:
                    ans += S
    print(ans)

=======
Suggestion 8

def solve():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()

    score = 0
    for i in range(N):
        if i < K:
            if T[i] == 'r':
                score += P
            elif T[i] == 's':
                score += R
            elif T[i] == 'p':
                score += S
        else:
            if T[i] == 'r' and T[i-K] != 'r':
                score += P
            elif T[i] == 's' and T[i-K] != 's':
                score += R
            elif T[i] == 'p' and T[i-K] != 'p':
                score += S

    print(score)

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = list(input())
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
            if t[i] == "r":
                if t[i-k] == "r":
                    t[i] = ""
                else:
                    ans += p
            elif t[i] == "s":
                if t[i-k] == "s":
                    t[i] = ""
                else:
                    ans += r
            else:
                if t[i-k] == "p":
                    t[i] = ""
                else:
                    ans += s
    print(ans)
