Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if S[i] != S[j] and S[i] != S[k] and S[j] != S[k] and j-i != k-j:
                    ans += 1
    print(ans)
main()

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if S[i] != S[j] and S[i] != S[k] and S[j] != S[k] and j-i != k-j:
                    ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if S[i] != S[j] and S[i] != S[k] and S[j] != S[k] and j-i != k-j:
                    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    R = S.count("R")
    G = S.count("G")
    B = S.count("B")
    ans = R*G*B
    for i in range(N-2):
        for j in range(i+1,N-1):
            k = j + (j-i)
            if k >= N:
                break
            if S[i] != S[j] and S[j] != S[k] and S[i] != S[k]:
                ans -= 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if S[i] == S[j]:
                continue
            k = j + (j - i)
            if k >= N:
                break
            if S[i] != S[k] and S[j] != S[k]:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    R = 0
    G = 0
    B = 0
    for s in S:
        if s == "R":
            R += 1
        elif s == "G":
            G += 1
        else:
            B += 1
    ans = R * G * B
    for i in range(N):
        for j in range(i + 1, N):
            if S[i] != S[j]:
                if i + (j - i) * 2 < N:
                    if S[i] != S[i + (j - i) * 2] and S[j] != S[i + (j - i) * 2]:
                        ans -= 1
                if i - (j - i) >= 0:
                    if S[i] != S[i - (j - i)] and S[j] != S[i - (j - i)]:
                        ans -= 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    s = list(input())
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if s[i] != s[j] and s[i] != s[k] and s[j] != s[k] and j-i != k-j:
                    ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    print(N*(N-1)*(N-2)//6 - S.count('R')*S.count('G')*S.count('B') - sum((S[i] != S[j]) * (S[j] != S[k]) * (S[k] != S[i]) * (k-j) * (j-i) for i in range(N) for j in range(i+1, N) for k in range(j+1, N)))

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    #print(n, s)
    r = 0
    g = 0
    b = 0
    for i in range(n):
        if s[i] == 'R':
            r += 1
        elif s[i] == 'G':
            g += 1
        else:
            b += 1
    #print(r, g, b)
    ans = r * g * b
    for i in range(n):
        for j in range(i + 1, n):
            k = j + j - i
            if k >= n:
                break
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans -= 1
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    s = input()

    # 各文字の個数をカウント
    cnt = [0, 0, 0]
    for i in range(n):
        if s[i] == 'R':
            cnt[0] += 1
        elif s[i] == 'G':
            cnt[1] += 1
        else:
            cnt[2] += 1

    # 各文字の個数の組み合わせを計算
    ans = cnt[0] * cnt[1] * cnt[2]

    # 3文字の組み合わせを計算
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]:
                continue
            if j + (j - i) < n and s[j] != s[j + (j - i)]:
                ans -= 1

    print(ans)
