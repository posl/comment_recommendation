Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    S = input()
    happy = 0
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            happy += 1
    print(min(happy + 2 * K, N - 1))

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            ans += 1
    print(min(ans+2*K, N-1))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(1, N):
        if S[i - 1] == S[i]:
            ans += 1
    ans = min(ans + 2 * K, N - 1)
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    s = input()
    if s.count("L") == 0 or s.count("R") == 0:
        print(n - 1)
        return
    if s[0] == "R":
        s = "L" + s
    if s[-1] == "L":
        s = s + "R"
    s = s.replace("LR", "L R")
    s = s.replace("RL", "R L")
    s = s.split()
    for i in range(len(s)):
        if s[i][0] == "R":
            s[i] = s[i][1:]
        if s[i][-1] == "L":
            s[i] = s[i][:-1]
    s = [i for i in s if len(i) > 0]
    if len(s) <= k:
        print(n)
        return
    ans = 0
    for i in range(k + 1):
        ans += len(s[i])
    print(ans)

main()

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    S = input()
    L = [0]
    for i in range(1, N):
        if S[i-1] != S[i]:
            L.append(i)
    L.append(N)
    ans = 0
    for i in range(len(L)-1):
        ans += min(L[i+1]-L[i], 2*K+1)
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if i == 0:
            ans += 1
        elif S[i] == S[i-1]:
            ans += 1
    print(min(ans + K * 2, N))

=======
Suggestion 7

def main():
    # Input
    N, K = map(int, input().split())
    S = input()
    # Solve
    ans = 0
    for i in range(N):
        if i == 0:
            if S[i] == S[i+1]:
                ans += 1
            else:
                ans += 2
        elif i == N-1:
            if S[i] == S[i-1]:
                ans += 1
            else:
                ans += 2
        else:
            if S[i] == S[i-1] and S[i] == S[i+1]:
                ans += 1
            elif S[i] == S[i-1] or S[i] == S[i+1]:
                ans += 2
            else:
                ans += 3
    ans = min(ans, 2*N-1)
    ans -= 2*K
    ans = max(0, ans)
    # Output
    print(ans)

=======
Suggestion 8

def main():
    N,K = map(int,input().split())
    S = input()
    S = S.replace("RL","X")
    S = S.replace("LR","Y")
    S = S.replace("R","0")
    S = S.replace("L","1")
    S = S.replace("X","10")
    S = S.replace("Y","01")
    happy = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            happy += 1
    happy += min(2*K,2*N-2*happy-1)
    print(happy)

=======
Suggestion 9

def solve(n, k, s):
    # n: the number of people
    # k: the number of operations
    # s: the directions of the people
    # return the maximum possible number of happy people after at most k operations.
    # 1. count the number of groups of Ls and Rs
    # 2. count the number of groups of Ls and Rs in the middle of Ls and Rs
    # 3. count the number of groups of Ls and Rs in the middle of Ls and Rs and Ls and Rs
    # 4. count the number of groups of Ls and Rs in the middle of Ls and Rs and Ls and Rs and Ls and Rs
    # ...
    # 5. count the number of groups of Ls and Rs in the middle of Ls and Rs and Ls and Rs and Ls and Rs and Ls and Rs
    # 6. count the number of groups of Ls and Rs in the middle of Ls and Rs and Ls and Rs and Ls and Rs and Ls and Rs and Ls and Rs
    # 7. count the number of groups of Ls and Rs in the middle of Ls and Rs and Ls and Rs and Ls and Rs and Ls and Rs and Ls and Rs and Ls and Rs
    # 8. count the number of

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    S = input()

    # 連続するLの数とRの数をそれぞれリストに格納する
    LR = []
    LR.append(0)
    if S[0] == 'L':
        LR.append(-1)
    else:
        LR.append(1)
    for i in range(1, N):
        if S[i] == 'L':
            LR.append(LR[-1] - 1)
        else:
            LR.append(LR[-1] + 1)

    # LRを並び替えて、連続するLの数とRの数が大きい方を選ぶ
    LR.sort()
    ans = 0
    for i in range(K + 1):
        ans = max(ans, LR[-i] - LR[i])

    # 連続するLの数とRの数のうち、小さい方を選ぶ
    ans = max(ans, min(LR[-K - 1], -LR[K + 1]))

    # 答えを出力する
    print(ans)
