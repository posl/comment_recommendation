Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = r * g * b
    for i in range(n):
        for j in range(i + 1, n):
            if j + (j - i) < n and s[i] != s[j] and s[j] != s[j + (j - i)] and s[i] != s[j + (j - i)]:
                ans -= 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    R = 0
    G = 0
    B = 0
    for i in range(N):
        if S[i] == "R":
            R += 1
        elif S[i] == "G":
            G += 1
        else:
            B += 1
    ans = R * G * B
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            k = 2 * j - i
            if k < N:
                if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                    ans -= 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    R = S.count('R')
    G = S.count('G')
    B = S.count('B')
    ans = R * G * B
    for i in range(N):
        for j in range(i+1, N):
            k = j + (j - i)
            if k >= N:
                continue
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    R = S.count("R")
    G = S.count("G")
    B = S.count("B")
    ans = R * G * B
    for i in range(N):
        for j in range(i+1, N):
            k = j + (j - i)
            if k >= N:
                continue
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    r_num = s.count('R')
    g_num = s.count('G')
    b_num = s.count('B')
    ans = r_num * g_num * b_num
    for i in range(n-2):
        for j in range(i+1, n-1):
            k = 2 * j - i
            if k >= n:
                continue
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans -= 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    R = S.count("R")
    G = S.count("G")
    B = S.count("B")

    ans = R * G * B

    for i in range(N-2):
        for j in range(i+1, N-1):
            k = j + (j - i)
            if k >= N:
                continue
            if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
                ans -= 1

    print(ans)

=======
Suggestion 7

def check(i,j,k):
    if s[i] != s[j] and s[i] != s[k] and s[j] != s[k] and j - i != k - j:
        return True
    else:
        return False

n = int(input())
s = list(input())
r = s.count("R")
g = s.count("G")
b = s.count("B")
ans = r * g * b
for i in range(n):
    for j in range(i+1,n):
        k = j + (j - i)
        if k < n and check(i,j,k):
            ans -= 1
print(ans)

=======
Suggestion 8

def solve():
    N = int(input())
    S = input()
    cnt = 0
    for i in range(N):
        for j in range(i+1,N):
            if S[i] == S[j]: continue
            k = j + (j - i)
            if k >= N: continue
            if S[i] == S[k] or S[j] == S[k]: continue
            cnt += 1
    print(cnt)

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    R = S.count('R')
    G = S.count('G')
    B = S.count('B')

    #print(R,G,B)
    ans = R * G * B
    #print(ans)
    for i in range(N):
        for j in range(i+1,N):
            k = j + (j-i)
            if k >= N:
                break
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1
    print(ans)

=======
Suggestion 10

def solve():
    N = int(input())
    S = input()
    
    # 2つの条件を満たす組の数を求める
    # 1つ目の条件を満たす組の数を求める
    # 2つ目の条件を満たす組の数を求める
    # 1つ目の条件を満たす組の数 - 2つ目の条件を満たす組の数
    
    # 1つ目の条件を満たす組の数を求める
    # R,G,Bの出現回数を数える
    R_cnt = 0
    G_cnt = 0
    B_cnt = 0
    for i in range(N):
        if S[i] == "R":
            R_cnt += 1
        elif S[i] == "G":
            G_cnt += 1
        else:
            B_cnt += 1
    
    # 1つ目の条件を満たす組の数を求める
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if S[i] != S[j]:
                if S[i] == "R":
                    if S[j] == "G":
                        count += B_cnt
                    else:
                        count += G_cnt
                elif S[i] == "G":
                    if S[j] == "R":
                        count += B_cnt
                    else:
                        count += R_cnt
                else:
                    if S[j] == "R":
                        count += G_cnt
                    else:
                        count += R_cnt
    
    # 2つ目の条件を満たす組の数を求める
    for i in range(N):
        for j in range(i+1, N):
            k = 2 * j - i
            if k >= N:
                continue
            if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
                count -= 1
    
    print(count)
