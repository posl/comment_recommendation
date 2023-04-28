Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def readinput():
    h,w=map(int,input().split())
    s=[]
    for _ in range(h):
        s.append(input())
    t=[]
    for _ in range(h):
        t.append(input())
    return h,w,s,t

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if s[i][j] != t[i][j]:
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] != T[i][j]:
                print("No")
                return
    print("Yes")

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
    print(S)
    print(T)
    S = sorted(S)
    T = sorted(T)
    print(S)
    print(T)
    if S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    S = []
    T = []
    for i in range(H):
        S.append(input())
    for i in range(H):
        T.append(input())
    S = sorted(S)
    T = sorted(T)
    if S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    s = []
    t = []
    for i in range(h):
        s.append(input())
    for i in range(h):
        t.append(input())
    s = sorted(s)
    t = sorted(t)
    for i in range(h):
        if s[i] != t[i]:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    T = [input() for i in range(H)]
    for i in range(H):
        if S[i].count('#') != T[i].count('#'):
            return False
    return True

=======
Suggestion 8

def solve():
    h,w = map(int,input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if s[i][j] != t[i][j]:
                break
        else:
            continue
        break
    else:
        print('Yes')
        exit()
    for i in range(h):
        for j in range(w):
            if s[i][j] != t[i][j]:
                break
        else:
            continue
        break
    else:
        print('No')
        exit()
    for i in range(h):
        for j in range(w):
            if s[i][j] != t[i][j]:
                break
        else:
            continue
        break
    else:
        print('Yes')
        exit()
    print('No')
solve()

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]

    #print(S)
    #print(T)

    for i in range(H):
        for j in range(W):
            if S[i][j] != T[i][j]:
                print('No')
                return

    print('Yes')
