Synthesizing 10/10 solutions

=======
Suggestion 1

def resolve():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    s = ["".join(sorted(s[i])) for i in range(h)]
    t = ["".join(sorted(t[i])) for i in range(h)]
    s.sort()
    t.sort()
    if s == t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    S_count = [[0] * W for _ in range(H)]
    T_count = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                S_count[i][j] = 1
            else:
                S_count[i][j] = 0
            if T[i][j] == "#":
                T_count[i][j] = 1
            else:
                T_count[i][j] = 0
    S_sum = sum([sum(i) for i in S_count])
    T_sum = sum([sum(i) for i in T_count])
    if S_sum != T_sum:
        print("No")
    else:
        print("Yes")

=======
Suggestion 3

def solve():
    H, W = map(int, input().split())

    S = []
    for i in range(H):
        S.append(input())

    T = []
    for i in range(H):
        T.append(input())

    if S == T:
        print("Yes")
        return

    for i in range(H-1):
        for j in range(W-1):
            if S[i][j] != T[i][j]:
                if S[i][j] == T[i+1][j+1] and S[i+1][j+1] == T[i][j]:
                    S[i] = S[i][:j] + T[i][j] + S[i][j+1:]
                    S[i+1] = S[i+1][:j+1] + T[i+1][j+1] + S[i+1][j+2:]
                    S[i] = S[i][:j+1] + T[i+1][j] + S[i][j+2:]
                    S[i+1] = S[i+1][:j] + T[i][j+1] + S[i+1][j+1:]
                    if S == T:
                        print("Yes")
                        return
                    else:
                        print("No")
                        return
                else:
                    print("No")
                    return
    print("No")

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    S = [list(s) for s in S]
    T = [list(t) for t in T]
    #print(S)
    #print(T)
    #print(S[0][0])
    #print(S[0][1])
    #print(S[1][0])
    #print(S[1][1])
    #print(S[2][0])
    #print(S[2][1])
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(T[0])
    #print(T[1])
    #print(T[2])
    #print(S[0][0])
    #print(S[0][1])
    #print(S[1][0])
    #print(S[1][1])
    #print(S[2][0])
    #print(S[2][1])
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(T[0])
    #print(T[1])
    #print(T[2])
    #print(S[0][0])
    #print(S[0][1])
    #print(S[1][0])
    #print(S[1][1])
    #print(S[2][0])
    #print(S[2][1])
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(T[0])
    #print(T[1])
    #print(T[2])
    #print(S[0][0])
    #print(S[0][1])
    #print(S[1][0])
    #print(S[1][1])
    #print(S[2][0])
    #print(S[2][1])
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(T[0])
    #print(T[1])
    #print(T[2])
    #print(S[0][0])
    #print(S[0][1])
    #print(S[1][0])
    #print(S[1][1])
    #print(S[2][0

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    S = [''.join(sorted(s)) for s in S]
    T = [''.join(sorted(t)) for t in T]
    S.sort()
    T.sort()
    if S == T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def is_same_shape(S, T):
    return sorted(S) == sorted(T)

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    T = [list(input()) for _ in range(H)]
    # print(S)
    # print(T)
    if S == T:
        print('Yes')
        return
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                # print(i,j)
                if 0 <= i-1 and 0 <= j-1 and S[i-1][j-1] == '#':
                    S[i-1][j-1] = '.'
                if 0 <= i-1 and S[i-1][j] == '#':
                    S[i-1][j] = '.'
                if 0 <= i-1 and j+1 <= W-1 and S[i-1][j+1] == '#':
                    S[i-1][j+1] = '.'
                if 0 <= j-1 and S[i][j-1] == '#':
                    S[i][j-1] = '.'
                if j+1 <= W-1 and S[i][j+1] == '#':
                    S[i][j+1] = '.'
                if i+1 <= H-1 and 0 <= j-1 and S[i+1][j-1] == '#':
                    S[i+1][j-1] = '.'
                if i+1 <= H-1 and S[i+1][j] == '#':
                    S[i+1][j] = '.'
                if i+1 <= H-1 and j+1 <= W-1 and S[i+1][j+1] == '#':
                    S[i+1][j+1] = '.'
    if S == T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    t = [list(input()) for _ in range(h)]
    s = [sorted(x) for x in s]
    t = [sorted(x) for x in t]
    s = sorted(s)
    t = sorted(t)
    for i in range(h):
        for j in range(w):
            if s[i][j] != t[i][j]:
                print('No')
                return
    print('Yes')

=======
Suggestion 9

def solve():
    H,W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    #print(H,W,S,T)
    S1 = ["".join(sorted(s)) for s in S]
    T1 = ["".join(sorted(t)) for t in T]
    #print(S1)
    #print(T1)
    if S1 == T1:
        print("Yes")
    else:
        print("No")
    return 0

=======
Suggestion 10

def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10**9 + 7
    h,w = map(int,readline().split())
    s = [readline().rstrip().decode('utf-8') for _ in range(h)]
    t = [readline().rstrip().decode('utf-8') for _ in range(h)]
    s_cnt = [0]*w
    t_cnt = [0]*w
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                s_cnt[j] += 1
            if t[i][j] == '#':
                t_cnt[j] += 1
    s_cnt.sort()
    t_cnt.sort()
    for i in range(w):
        if s_cnt[i] != t_cnt[i]:
            print('No')
            exit()
    print('Yes')
