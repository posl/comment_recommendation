Synthesizing 10/10 solutions

=======
Suggestion 1

def readinput():
    h,w=list(map(int,input().split()))
    s=[]
    for i in range(h):
        s.append(input())
    t=[]
    for i in range(h):
        t.append(input())
    return h,w,s,t

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    print('Yes' if sorted(S) == sorted(T) else 'No')

=======
Suggestion 3

def main():
    h,w = map(int,input().split())
    s = [input() for i in range(h)]
    t = [input() for i in range(h)]
    for i in range(h):
        for j in range(w):
            if s[i][j] != t[i][j]:
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    ss = []
    tt = []
    for i in range(h):
        ss.append(sorted(s[i]))
        tt.append(sorted(t[i]))
    ss.sort()
    tt.sort()
    for i in range(h):
        if ss[i] != tt[i]:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    s = []
    t = []
    for i in range(H):
        s.append(set([S[i][j] for j in range(W)]))
        t.append(set([T[i][j] for j in range(W)]))
    for i in range(H):
        if s[i] != t[i]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 6

def main():
    H,W = map(int,input().split())
    S = []
    T = []
    for i in range(H):
        S.append(input())
    for i in range(H):
        T.append(input())
    S = sorted(S)
    T = sorted(T)
    flag = True
    for i in range(H):
        if S[i] != T[i]:
            flag = False
    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    h,w = map(int,input().split())
    s = [input() for i in range(h)]
    t = [input() for i in range(h)]
    s2 = []
    t2 = []
    for i in range(h):
        s2.append("".join(sorted(s[i])))
        t2.append("".join(sorted(t[i])))
    s2.sort()
    t2.sort()
    for i in range(h):
        if s2[i] != t2[i]:
            print("No")
            return
    for i in range(h):
        for j in range(w):
            if s[i][j] != t[i][j]:
                if t[i][j] == "#":
                    print("No")
                    return
                else:
                    for k in range(h):
                        if s[k][j] == "#":
                            print("No")
                            return
                    break
    print("Yes")
    return

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    s_ = []
    for i in range(h):
        temp = []
        for j in range(w):
            if s[i][j] == '#':
                temp.append(j)
        s_.append(temp)
    t_ = []
    for i in range(h):
        temp = []
        for j in range(w):
            if t[i][j] == '#':
                temp.append(j)
        t_.append(temp)
    s_.sort()
    t_.sort()
    if s_ == t_:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def calc():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    for i in range(H):
        if S[i].count('#') != T[i].count('#'):
            print('No')
            return
    for j in range(W):
        if [S[i][j] for i in range(H)].count('#') != [T[i][j] for i in range(H)].count('#'):
            print('No')
            return
    print('Yes')
    return

calc()

=======
Suggestion 10

def check_pattern(S, T):
    for i in range(len(S)):
        if S[i] != T[i]:
            return False
    return True
