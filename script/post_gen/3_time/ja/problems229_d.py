Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    k = int(input())
    n = len(s)
    ans = 0
    l = 0
    r = 0
    while r < n:
        while r < n and s[r] == "X":
            r += 1
        ans = max(ans, r - l)
        if r == n:
            break
        l = r
        while r < n and r - l < k and s[r] == ".":
            r += 1
        if r == n:
            break
        if s[r] == "X":
            r += 1
        l = r
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    K = int(input())
    S = S + "X"
    S_list = []
    count = 0
    for i in range(len(S)):
        if S[i] == "X":
            if count != 0:
                S_list.append(count)
                count = 0
        else:
            count += 1
    if len(S_list) <= K:
        print(len(S) - 1)
    else:
        S_list.sort()
        print(len(S) - 1 - sum(S_list[:K]))

=======
Suggestion 3

def main():
    s = input()
    k = int(input())
    s = s.replace(".","")
    if len(s) == 0:
        print(0)
        return
    if k == 0:
        print(len(s))
        return
    ans = 0
    for i in range(len(s)-k):
        ans = max(ans,len(s[i:i+k+1]))
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    K = int(input())
    N = len(S)
    X = 0
    Y = 0
    Z = 0
    if N == 1:
        print(1)
        return
    for i in range(N):
        if S[i] == 'X':
            X += 1
        else:
            Y += 1
            Z = max(Z, Y)
            if Y > K:
                Y = 0
    print(X + Z)

=======
Suggestion 5

def main():
    S = input()
    K = int(input())
    #print(S)
    #print(K)
    #print(len(S))
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(S[3])
    #print(S[4])
    #print(S[5])
    #print(S[6])
    #print(S[7])
    #print(S[8])
    #print(S[9])
    #print(S[10])
    #print(S[11])
    #print(S[12])
    #print(S[13])
    #print(S[14])
    #print(S[15])
    #print(S[16])

    #Xを連続させる最大数を求める
    #Xの連続数を数える
    X_count = 0
    for i in range(len(S)):
        if S[i] == "X":
            X_count += 1
        else:
            break
    for i in range(len(S)-1, -1, -1):
        if S[i] == "X":
            X_count += 1
        else:
            break
    #print(X_count)
    #Xの連続数がSの長さと同じなら、Xを連続させる最大数はSの長さ
    if X_count == len(S):
        print(len(S))
        return
    #Xの連続数がSの長さと同じでないなら、Xを連続させる最大数はXの連続数+K
    else:
        print(X_count+K)

=======
Suggestion 6

def solve():
    s = input()
    k = int(input())
    n = len(s)
    if n == 1:
        print(1)
        return
    if s[0] == s[-1] and s[0] == 'X':
        r = 0
        for i in range(n):
            if s[i] == 'X':
                r += 1
            else:
                break
        l = 0
        for i in range(n-1, -1, -1):
            if s[i] == 'X':
                l += 1
            else:
                break
        print(min(n, r+l+k*2))
    else:
        r = 0
        for i in range(n):
            if s[i] == 'X':
                r += 1
            else:
                break
        l = 0
        for i in range(n-1, -1, -1):
            if s[i] == 'X':
                l += 1
            else:
                break
        print(min(n, r+l+k*2-1))

solve()

=======
Suggestion 7

def main():
    s = input()
    k = int(input())
    if k == 0:
        print(len(max(s.split('.'), key=len)))
        return
    cnt = 0
    for i in range(len(s)):
        if s[i] == 'X':
            cnt += 1
        else:
            if cnt >= k:
                break
            cnt = 0
    print(cnt + k)

=======
Suggestion 8

def main():
    S = input()
    K = int(input())
    S = S.replace('.', 'X')
    print(S)
    print(K)

=======
Suggestion 9

def main():
    S = input()
    K = int(input())
    S = S.replace('.','X')
    S = S.replace('X','.')
    print(S)
    print(K)

=======
Suggestion 10

def main():
    S = input()
    K = int(input())
    N = len(S)
    # X が連続する部分をまとめる
    X = []
    cnt = 0
    for i in range(N):
        if S[i] == "X":
            cnt += 1
        else:
            if cnt > 0:
                X.append(cnt)
            cnt = 0
    if cnt > 0:
        X.append(cnt)
    # X が連続する部分のうち、K 個以上連続する部分を削除する
    M = len(X)
    for i in range(M):
        if X[i] <= K:
            K -= X[i]
            X[i] = 0
        else:
            X[i] -= K
            break
    # X が連続する部分の長さの和が答え
    ans = sum(X)
    print(ans)
