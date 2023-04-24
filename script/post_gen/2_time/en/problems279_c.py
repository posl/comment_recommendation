Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    for i in range(H):
        S[i] = S[i] + S[i]
    for i in range(H):
        T[i] = T[i] + T[i]
    for i in range(H):
        if S[i] not in T:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] != T[i][j]:
                break
        else:
            continue
        break
    else:
        print("Yes")
        return
    if H % 2 == 0 and W % 2 == 0:
        print("No")
        return
    if H % 2 == 0:
        for i in range(H):
            for j in range(W//2):
                if S[i][j] != S[i][W-1-j]:
                    break
            else:
                continue
            break
        else:
            print("Yes")
            return
        for i in range(H):
            for j in range(W//2):
                if T[i][j] != T[i][W-1-j]:
                    break
            else:
                continue
            break
        else:
            print("Yes")
            return
        print("No")
        return
    if W % 2 == 0:
        for i in range(H//2):
            for j in range(W):
                if S[i][j] != S[H-1-i][j]:
                    break
            else:
                continue
            break
        else:
            print("Yes")
            return
        for i in range(H//2):
            for j in range(W):
                if T[i][j] != T[H-1-i][j]:
                    break
            else:
                continue
            break
        else:
            print("Yes")
            return
        print("No")
        return
    for i in range(H//2):
        for j in range(W//2):
            if S[i][j] != S[H-1-i][W-1-j]:
                break
        else:
            continue
        break
    else:
        print("Yes")
        return
    for i in range(H//2):
        for j in range(W//2):
            if T[i][j] != T[H-1-i][W-1-j]:
                break
        else:
            continue
        break
    else:
        print("Yes")
        return
    print("No")
    return

main()

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] != T[i][j]:
                break
        else:
            continue
        break
    else:
        print('Yes')
        exit()
    for i in range(H):
        for j in range(W):
            if S[i][j] != T[i][j]:
                break
        else:
            continue
        break
    else:
        print('Yes')
        exit()
    for i in range(H):
        for j in range(W):
            if S[i][j] != T[i][j]:
                break
        else:
            continue
        break
    else:
        print('Yes')
        exit()
    for i in range(H):
        for j in range(W):
            if S[i][j] != T[i][j]:
                break
        else:
            continue
        break
    else:
        print('Yes')
        exit()
    for i in range(H):
        for j in range(W):
            if S[i][j] != T[i][j]:
                break
        else:
            continue
        break
    else:
        print('Yes')
        exit()
    for i in range(H):
        for j in range(W):
            if S[i][j] != T[i][j]:
                break
        else:
            continue
        break
    else:
        print('Yes')
        exit()
    for i in range(H):
        for j in range(W):
            if S[i][j] != T[i][j]:
                break
        else:
            continue
        break
    else:
        print('Yes')
        exit()
    for i in range(H):
        for j in range(W):
            if S[i][j] != T[i][j]:
                break
        else:
            continue
        break
    else:
        print('Yes')
        exit()
    for i in range(H):
        for j in range(W):
            if S[i][j] != T[i][j]:
                break
        else:
            continue
        break
    else:
        print('Yes')
        exit()
    for i in range(H):
        for j in range

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    for i in range(H):
        S[i] = ''.join(sorted(S[i]))
        T[i] = ''.join(sorted(T[i]))
    S.sort()
    T.sort()
    if S == T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    s = [input() for i in range(h)]
    t = [input() for i in range(h)]
    for i in range(h):
        s[i] = list(s[i])
        t[i] = list(t[i])
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                s[i][j] = 1
            else:
                s[i][j] = 0
            if t[i][j] == '#':
                t[i][j] = 1
            else:
                t[i][j] = 0
    for i in range(w):
        for j in range(i, w):
            s2 = [s[i][j] for i in range(h)]
            s2.sort()
            t2 = [t[i][j] for i in range(h)]
            t2.sort()
            if s2 == t2:
                for k in range(i + 1, w):
                    s2 = [s[i][k] for i in range(h)]
                    s2.sort()
                    t2 = [t[i][k] for i in range(h)]
                    t2.sort()
                    if s2 != t2:
                        print('No')
                        return
                print('Yes')
                return
    print('No')

=======
Suggestion 6

def solve():
    H,W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                S[i] = S[i][:j] + '1' + S[i][j+1:]
                T[i] = T[i][:j] + '1' + T[i][j+1:]
            else:
                S[i] = S[i][:j] + '0' + S[i][j+1:]
                T[i] = T[i][:j] + '0' + T[i][j+1:]
    S.sort()
    T.sort()
    if S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    H,W = map(int,input().split())
    S = []
    T = []
    for i in range(H):
        S.append(input())
    for i in range(H):
        T.append(input())
    print(S)
    print(T)

    if H == 1:
        if S[0] == T[0]:
            print("Yes")
            return
        else:
            print("No")
            return
    if W == 1:
        for i in range(H):
            if S[i][0] != T[i][0]:
                print("No")
                return
        print("Yes")
        return

    S_ = []
    T_ = []
    for i in range(H):
        S_.append(list(S[i]))
        T_.append(list(T[i]))
    print(S_)
    print(T_)

    for i in range(W):
        for j in range(i+1,W):
            if S_[0][i] == S_[0][j]:
                if T_[0][i] == T_[0][j]:
                    continue
                else:
                    print("No")
                    return
            else:
                if T_[0][i] == T_[0][j]:
                    S_[0][i],S_[0][j] = S_[0][j],S_[0][i]
                    continue
                else:
                    print("No")
                    return
    print(S_)
    print(T_)
    for i in range(H):
        for j in range(W):
            if S_[i][j] == T_[i][j]:
                continue
            else:
                print("No")
                return
    print("Yes")

=======
Suggestion 8

def main():
    H,W = map(int,input().split())
    S = [input() for i in range(H)]
    T = [input() for i in range(H)]
    if H == 1:
        if S[0] == T[0]:
            print("Yes")
        else:
            print("No")
        return
    if W == 1:
        if S == T:
            print("Yes")
        else:
            print("No")
        return
    if H % 2 == 0 and W % 2 == 0:
        for i in range(H):
            if S[i] != T[i]:
                print("No")
                return
        print("Yes")
        return
    if H % 2 == 1 and W % 2 == 1:
        for i in range(H):
            if S[i] != T[i]:
                print("No")
                return
        print("Yes")
        return
    if H % 2 == 1 and W % 2 == 0:
        for i in range(H):
            if S[i] != T[i]:
                print("No")
                return
        print("Yes")
        return
    if H % 2 == 0 and W % 2 == 1:
        for i in range(H):
            if S[i] != T[i]:
                print("No")
                return
        print("Yes")
        return

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]

    for p in permutations(range(W), W):
        S_ = ["".join(S[i][p[j]] for j in range(W)) for i in range(H)]
        if S_ == T:
            print("Yes")
            return
    print("No")

=======
Suggestion 10

def main():
    import sys
    from collections import Counter
    input = sys.stdin.readline
    H,W = map(int,input().split())
    S = [input().rstrip() for _ in range(H)]
    T = [input().rstrip() for _ in range(H)]
    if Counter(S) == Counter(T):
        print("Yes")
    else:
        print("No")
    return
