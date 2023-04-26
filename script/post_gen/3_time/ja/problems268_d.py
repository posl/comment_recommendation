Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    for i in range(3, 17):
        for s in product(S, repeat=i):
            s = ''.join(s)
            if len(s) != i: continue
            if s in T: continue
            print(s)
            return
    print(-1)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]

    if N == 1:
        for i in range(3, 17):
            for j in range(1, i):
                X = S[0] + '_' * j
                if X not in T:
                    print(X)
                    return
        print(-1)
        return

    for i in range(3, 17):
        for j in range(1, i):
            for k in range(1, i):
                X = S[0] + '_' * j + S[1] + '_' * k
                if X not in T:
                    print(X)
                    return
    print(-1)

=======
Suggestion 3

def main():
    # input
    N, M = map(int, input().split())
    Ss = [input() for _ in range(N)]
    Ts = [input() for _ in range(M)]

    # compute
    """WRITE BELOW"""

    # output

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    ans = ''
    for i in range(N):
        ans += S[i] + '_'
    ans = ans[:-1]
    if ans in T:
        print(-1)
    else:
        print(ans)

=======
Suggestion 5

def main():
    import itertools
    N, M = map(int, input().split())
    S = []
    T = []
    for i in range(N):
        S.append(input())
    for i in range(M):
        T.append(input())
    for i in range(3, 17):
        L = list(itertools.product(S, repeat=i))
        for j in range(len(L)):
            X = ''.join(L[j])
            for k in range(M):
                if X == T[k]:
                    break
                elif k == M-1:
                    print(X)
                    return
    print(-1)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    ans = []
    for s in S:
        ans.append(s)
        ans.append('_')
    ans.pop()
    ans = ''.join(ans)
    if ans in T:
        print(-1)
    else:
        print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    if N == 1:
        if S[0] in T:
            print(-1)
        else:
            print(S[0])
        return
    if N == 2:
        for i in range(1, 16):
            for j in range(1, 16):
                if i + j + len(S[0]) + len(S[1]) == 16:
                    X = S[0] + "_" * i + S[1] + "_" * j
                    if X not in T:
                        print(X)
                        return
        print(-1)
        return
    if N == 3:
        for i in range(1, 16):
            for j in range(1, 16):
                for k in range(1, 16):
                    if i + j + k + len(S[0]) + len(S[1]) + len(S[2]) == 16:
                        X = S[0] + "_" * i + S[1] + "_" * j + S[2] + "_" * k
                        if X not in T:
                            print(X)
                            return
        print(-1)
        return
    if N == 4:
        for i in range(1, 16):
            for j in range(1, 16):
                for k in range(1, 16):
                    for l in range(1, 16):
                        if i + j + k + l + len(S[0]) + len(S[1]) + len(S[2]) + len(S[3]) == 16:
                            X = S[0] + "_" * i + S[1] + "_" * j + S[2] + "_" * k + S[3] + "_" * l
                            if X not in T:
                                print(X)
                                return
        print(-1)
        return
    if N == 5:
        for i in range(1, 16):
            for j in range(1, 16):
                for k in range(1, 16):
                    for l in range(1, 16):
                        for m in range(1, 16):
                            if i +

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    X = ""

    for i in range(N):
        X += S[i]
        if i != N-1:
            X += "_"

    if X in T:
        print(-1)
    else:
        print(X)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    X = ''.join(S)
    for i in range(3, 17):
        for j in range(0, N):
            for k in range(0, N):
                if j == k: continue
                if X == ''.join(S[j:j+1] + ['_'] * i + S[k:k+1]):
                    if X not in T:
                        print(X)
                        return
    print('-1')

=======
Suggestion 10

def getNum():
    return map(int, input().split())
