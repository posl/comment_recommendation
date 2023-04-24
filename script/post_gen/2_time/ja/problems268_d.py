Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for k in range(N):
                if k == i or k == j:
                    continue
                for l in range(N):
                    if l == i or l == j or l == k:
                        continue
                    X = S[i] + "_" + S[j] + "_" + S[k] + "_" + S[l]
                    X = X.replace("____", "_")
                    X = X.replace("___", "_")
                    X = X.replace("__", "_")
                    if len(X) < 4 or len(X) > 16:
                        continue
                    if X not in T:
                        print(X)
                        return
    print(-1)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    for i in range(N):
        for j in range(M):
            if S[i] in T[j]:
                print(-1)
                return
    for i in range(2**N):
        x = ''
        for j in range(N):
            if (i >> j) & 1:
                x += S[j] + '_'
            else:
                x += '_' + S[j]
        if 3 <= len(x) <= 16:
            for j in range(M):
                if x == T[j]:
                    break
            else:
                print(x)
                return
    print(-1)

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]

    for i in range(N):
        for j in range(i + 1, N):
            if S[i] in T or S[j] in T:
                continue

            for k in range(1, 17 - len(S[i]) - len(S[j]) + 1):
                X = S[i] + "_" * k + S[j]
                if X not in T:
                    print(X)
                    return
    print(-1)

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    for i in range(3, 17):
        for j in range(1 << (i - 1)):
            X = ''
            for k in range(N):
                if k > 0:
                    for l in range(i - 1):
                        if j >> l & 1:
                            X += '_'
                X += S[k]
            if len(X) != i:
                continue
            if X in T:
                continue
            print(X)
            return
    print(-1)

=======
Suggestion 5

def solve():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(n):
                if k == i or k == j:
                    continue
                for l in range(n):
                    if l == i or l == j or l == k:
                        continue
                    x = s[i] + "_" + s[j] + "_" + s[k] + "_" + s[l]
                    if len(x) > 16:
                        continue
                    if x in t:
                        continue
                    print(x)
                    return
    print(-1)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    ans = ""
    for i in range(3, 17):
        for j in range(2 ** (i - 1)):
            tmp = ""
            for k in range(i - 1):
                if j >> k & 1:
                    tmp += "_"
                tmp += S[k]
            tmp += S[i - 1]
            if tmp not in T:
                ans = tmp
                break
        if ans:
            break
    print(ans if ans else -1)

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    for i in range(1, N):
        S[i] = '_' + S[i]
    ans = ''.join(S)
    if ans in T:
        print(-1)
    else:
        print(ans)

=======
Suggestion 8

def solve():
    N, M = list(map(int, input().split()))
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    for i in range(2 ** N):
        x = []
        for j in range(N):
            if (i >> j) & 1:
                x.append(S[j])
            else:
                x.append("_" * len(S[j]))
        X = "".join(x)
        if 3 <= len(X) <= 16 and X not in T:
            print(X)
            return
    print(-1)

=======
Suggestion 9

def main():
    # 入力
    N, M = list(map(int, input().split()))
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]

    # 処理
    def is_ok(x):
        for t in T:
            if t == x:
                return False
        return True

    def dfs(s):
        if len(s) > 16:
            return
        if is_ok(s):
            print(s)
            exit()
        for i in range(N):
            dfs(s + "_" + S[i])
        return

    # 出力
    dfs("")
    print(-1)

=======
Suggestion 10

def main():
    N,M = map(int,input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]

    X = ""
    for s in S:
        X += s
        X += "_"
    X = X[:-1]
    if len(X) < 3 or 16 < len(X):
        print(-1)
        return

    for t in T:
        if X == t:
            print(-1)
            return

    print(X)
