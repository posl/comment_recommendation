Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H,W = map(int,input().split())
    S = []
    T = []
    for i in range(H):
        S.append(input())
    for i in range(H):
        T.append(input())
    S.sort()
    T.sort()
    if S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]

    if H == 1 or W == 1:
        if S == T:
            print("Yes")
        else:
            print("No")
        return

    for i in range(H-1):
        for j in range(W-1):
            if S[i][j:j+2] == T[i][j:j+2] and S[i+1][j:j+2] == T[i+1][j:j+2]:
                continue
            elif S[i][j:j+2] == T[i+1][j:j+2] and S[i+1][j:j+2] == T[i][j:j+2]:
                continue
            else:
                print("No")
                return

    print("Yes")

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    if H == 1 and W == 1:
        if S[0] == T[0]:
            print('Yes')
        else:
            print('No')
        return

    if H == 1:
        for i in range(W):
            if S[0][i] == '#':
                for j in range(W):
                    if T[0][j] == '#':
                        if S[0][i:] + S[0][:i] == T[0][j:] + T[0][:j]:
                            print('Yes')
                            return
        print('No')
        return
    if W == 1:
        for i in range(H):
            if S[i][0] == '#':
                for j in range(H):
                    if T[j][0] == '#':
                        if S[i:] + S[:i] == T[j:] + T[:j]:
                            print('Yes')
                            return
        print('No')
        return

    for i in range(H):
        if S[i][0] == '#':
            for j in range(H):
                if T[j][0] == '#':
                    if S[i:] + S[:i] == T[j:] + T[:j]:
                        for k in range(W):
                            if S[i][k] == '#':
                                for l in range(W):
                                    if T[j][l] == '#':
                                        if S[i][k:] + S[i][:k] == T[j][l:] + T[j][:l]:
                                            print('Yes')
                                            return
    print('No')

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    S = []
    T = []
    for i in range(H):
        S.append(input())
    for i in range(H):
        T.append(input())
    #print(S)
    #print(T)
    for i in range(H):
        for j in range(W):
            if S[i][j] == T[i][j]:
                continue
            else:
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 5

def main():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    S = [list(s) for s in S]
    T = [list(t) for t in T]
    for i in range(H):
        for j in range(W):
            if S[i][j] == T[i][j]:
                continue
            else:
                if S[i][j] == '#':
                    S[i][j] = '.'
                else:
                    S[i][j] = '#'
                if i == 0:
                    if j == 0:
                        if S[i][j+1] == '#':
                            S[i][j+1] = '.'
                        else:
                            S[i][j+1] = '#'
                        if S[i+1][j] == '#':
                            S[i+1][j] = '.'
                        else:
                            S[i+1][j] = '#'
                    elif j == W-1:
                        if S[i][j-1] == '#':
                            S[i][j-1] = '.'
                        else:
                            S[i][j-1] = '#'
                        if S[i+1][j] == '#':
                            S[i+1][j] = '.'
                        else:
                            S[i+1][j] = '#'
                    else:
                        if S[i][j+1] == '#':
                            S[i][j+1] = '.'
                        else:
                            S[i][j+1] = '#'
                        if S[i][j-1] == '#':
                            S[i][j-1] = '.'
                        else:
                            S[i][j-1] = '#'
                        if S[i+1][j] == '#':
                            S[i+1][j] = '.'
                        else:
                            S[i+1][j] = '#'
                elif i == H-1:
                    if j == 0:
                        if S[i][j+1] == '#':
                            S[i][j+1] = '.'
                        else:
                            S[i][j+1] = '#'
                        if S[i-1][j] == '#':
                            S[i-1][j] = '.'
                        else:
                            S[i-1][j] = '#'
                    elif j

=======
Suggestion 6

def main():
    H,W = map(int,input().split())
    S = [input() for i in range(H)]
    T = [input() for i in range(H)]
    S = sorted(S)
    T = sorted(T)
    if S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    if H%2==0:
        if W%2==0:
            for i in range(H//2):
                for j in range(W//2):
                    if S[i][j]!=S[H-1-i][j] or S[i][j]!=S[i][W-1-j] or S[i][j]!=S[H-1-i][W-1-j]:
                        print("No")
                        return
                    if T[i][j]!=T[H-1-i][j] or T[i][j]!=T[i][W-1-j] or T[i][j]!=T[H-1-i][W-1-j]:
                        print("No")
                        return
        else:
            for i in range(H//2):
                for j in range(W//2):
                    if S[i][j]!=S[H-1-i][j] or S[i][j]!=S[i][W-1-j] or S[i][j]!=S[H-1-i][W-1-j]:
                        print("No")
                        return
                    if T[i][j]!=T[H-1-i][j] or T[i][j]!=T[i][W-1-j] or T[i][j]!=T[H-1-i][W-1-j]:
                        print("No")
                        return
            for i in range(H//2):
                if S[i][W//2]!=S[H-1-i][W//2] or T[i][W//2]!=T[H-1-i][W//2]:
                    print("No")
                    return
    else:
        if W%2==0:
            for i in range(H//2):
                for j in range(W//2):
                    if S[i][j]!=S[H-1-i][j] or S[i][j]!=S[i][W-1-j] or S[i][j]!=S[H-1-i][W-1-j]:
                        print("No")
                        return
                    if T[i][j]!=T[H-1-i][j] or T[i][j]!=T[i][W-1-j] or T[i][j]!=T[H-1-i][W-1-j]:
                        print("No")
                        return
            for

=======
Suggestion 8

def main():
    H,W=map(int,input().split())
    S=[input() for _ in range(H)]
    T=[input() for _ in range(H)]

    def check(S,T):
        for i in range(H):
            for j in range(W):
                if S[i][j]!=T[i][j]:
                    return False
        return True

    for i in range(W):
        for j in range(W):
            S2=[S[i][j] for i in range(H)]
            T2=[T[i][j] for i in range(H)]
            S2.sort()
            T2.sort()
            if S2==T2:
                if check(S,T):
                    print("Yes")
                    exit()
    print("No")

=======
Suggestion 9

def main():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    if H==1:
        if "".join(S)=="".join(T):
            print("Yes")
        else:
            print("No")
        return
    if W==1:
        if "".join(S)=="".join(T):
            print("Yes")
        else:
            print("No")
        return
    if H==2:
        for i in range(W):
            if S[0][i]+S[1][i]==T[0][i]+T[1][i]:
                continue
            else:
                print("No")
                return
        print("Yes")
        return
    if W==2:
        for i in range(H):
            if S[i][0]+S[i][1]==T[i][0]+T[i][1]:
                continue
            else:
                print("No")
                return
        print("Yes")
        return
    if H==3:
        for i in range(W):
            if S[0][i]+S[1][i]+S[2][i]==T[0][i]+T[1][i]+T[2][i]:
                continue
            else:
                print("No")
                return
        print("Yes")
        return
    if W==3:
        for i in range(H):
            if S[i][0]+S[i][1]+S[i][2]==T[i][0]+T[i][1]+T[i][2]:
                continue
            else:
                print("No")
                return
        print("Yes")
        return
    if H==4:
        for i in range(W):
            if S[0][i]+S[1][i]+S[2][i]+S[3][i]==T[0][i]+T[1][i]+T[2][i]+T[3][i]:
                continue
            else:
                print("No")
                return
        print("Yes")
        return
    if W==4:
        for i in range(H):
            if S[i][0]+S[i][1]+S[i][2]+S[i][3]==T[i][0]+T[i][1]+T[i][2]+T[i][3]:
                continue

=======
Suggestion 10

def solve():
    H,W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    #S,Tを縦に並べたものを比較する
    for i in range(W):
        s = [s[i] for s in S]
        t = [t[i] for t in T]
        if sorted(s) != sorted(t):
            print("No")
            return
    print("Yes")
