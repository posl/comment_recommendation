Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    for i in range(h):
        s[i] = s[i] + s[i]
    for i in range(h):
        t[i] = t[i] + t[i]
    for i in range(h):
        for j in range(w):
            if s[i][j:j+w] == t[i]:
                break
        else:
            print("No")
            break
    else:
        print("Yes")

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    for i in range(h):
        s[i] = list(s[i])
        t[i] = list(t[i])
    s.sort()
    t.sort()
    for i in range(h):
        for j in range(w):
            if s[i][j] != t[i][j]:
                print('No')
                return
    print('Yes')

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    if H % 2 == 0 and W % 2 == 0:
        for i in range(H):
            for j in range(W):
                if S[i][j] != T[i][j]:
                    print("No")
                    return
        print("Yes")
        return
    if H % 2 == 0:
        for i in range(H):
            for j in range(W // 2):
                if S[i][j] != T[i][j] or S[i][W - 1 - j] != T[i][W - 1 - j]:
                    print("No")
                    return
        print("Yes")
        return
    if W % 2 == 0:
        for i in range(H // 2):
            for j in range(W):
                if S[i][j] != T[i][j] or S[H - 1 - i][j] != T[H - 1 - i][j]:
                    print("No")
                    return
        print("Yes")
        return
    S1 = []
    S2 = []
    T1 = []
    T2 = []
    for i in range(H // 2):
        for j in range(W // 2):
            if S[i][j] != T[i][j] or S[i][W - 1 - j] != T[i][W - 1 - j] or S[H - 1 - i][j] != T[H - 1 - i][j] or S[H - 1 - i][W - 1 - j] != T[H - 1 - i][W - 1 - j]:
                print("No")
                return
            S1.append(S[i][j])
            S2.append(S[i][W - 1 - j])
            T1.append(T[i][j])
            T2.append(T[i][W - 1 - j])
    S1.sort()
    S2.sort()
    T1.sort()
    T2.sort()
    if S1 == T1 and S2 == T2:
        print("Yes")
        return
    print("No")

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    if sorted(s) == sorted(t):
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    T = [input() for i in range(H)]

    for i in range(H):
        if S[i] == T[i]:
            continue
        else:
            for j in range(W):
                if S[i][j] == T[i][j]:
                    continue
                else:
                    for k in range(H):
                        if S[k][j] == T[i][j]:
                            S[i], S[k] = S[k], S[i]
                            break
                    else:
                        print('No')
                        return
    print('Yes')

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    for i in range(w):
        s[i] = ''.join([s[j][i] for j in range(h)])
        t[i] = ''.join([t[j][i] for j in range(h)])
    s.sort()
    t.sort()
    print('Yes' if s == t else 'No')

=======
Suggestion 7

def main():
    H,W = map(int,input().split())
    S = [input() for h in range(H)]
    T = [input() for h in range(H)]
    if H%2==0 and W%2==0:
        if S==T:
            print("Yes")
            return
        else:
            print("No")
            return
    elif H%2==0:
        S = ["".join(S[h][w] for h in range(H)) for w in range(W)]
        T = ["".join(T[h][w] for h in range(H)) for w in range(W)]
        if S==T:
            print("Yes")
            return
        else:
            print("No")
            return
    elif W%2==0:
        S = ["".join(S[h][w] for w in range(W)) for h in range(H)]
        T = ["".join(T[h][w] for w in range(W)) for h in range(H)]
        if S==T:
            print("Yes")
            return
        else:
            print("No")
            return
    else:
        S = ["".join(S[h][w] for h in range(H)) for w in range(W)]
        T = ["".join(T[h][w] for h in range(H)) for w in range(W)]
        if S==T:
            print("Yes")
            return
        else:
            print("No")
            return

=======
Suggestion 8

def main():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    S1 = ["".join(sorted([S[i][j] for i in range(H)])) for j in range(W)]
    T1 = ["".join(sorted([T[i][j] for i in range(H)])) for j in range(W)]
    if S1 == T1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def solve():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    S = list(map(lambda x: list(x), S))
    T = list(map(lambda x: list(x), T))
    S = list(map(lambda x: list(map(lambda y: 1 if y == "#" else 0, x)), S))
    T = list(map(lambda x: list(map(lambda y: 1 if y == "#" else 0, x)), T))
    S = list(map(lambda x: list(map(lambda y: y%2, x)), S))
    T = list(map(lambda x: list(map(lambda y: y%2, x)), T))
    A = list(map(lambda x: x[0], S))
    B = list(map(lambda x: x[0], T))
    S = list(map(lambda x: x[1:], S))
    T = list(map(lambda x: x[1:], T))
    S = list(map(lambda x: sum(x), S))
    T = list(map(lambda x: sum(x), T))
    S = list(map(lambda x: x%2, S))
    T = list(map(lambda x: x%2, T))
    if A == B and S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    T = [list(input()) for _ in range(H)]

    def check():
        s = [0] * 26
        t = [0] * 26
        for i in range(H):
            for j in range(W):
                s[ord(S[i][j]) - 35] += 1
                t[ord(T[i][j]) - 35] += 1
        return s == t

    def rotate():
        s = [[0] * H for _ in range(W)]
        for i in range(H):
            for j in range(W):
                s[j][H - i - 1] = S[i][j]
        return s

    def flip():
        s = [[0] * W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                s[H - i - 1][j] = S[i][j]
        return s

    if check():
        print("Yes")
        return

    S = rotate()
    if check():
        print("Yes")
        return

    S = rotate()
    if check():
        print("Yes")
        return

    S = rotate()
    if check():
        print("Yes")
        return

    S = flip()
    if check():
        print("Yes")
        return

    S = rotate()
    if check():
        print("Yes")
        return

    S = rotate()
    if check():
        print("Yes")
        return

    S = rotate()
    if check():
        print("Yes")
        return

    print("No")

main()
