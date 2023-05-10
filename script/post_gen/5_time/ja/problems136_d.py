Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    for i in range(N):
        if S[i] == "R" and S[i + 1] == "L":
            Rpos = i
            Lpos = i + 1
            Rcnt = 0
            Lcnt = 0
            while S[Rpos] == "R":
                Rpos -= 1
                Rcnt += 1
            while S[Lpos] == "L":
                Lpos += 1
                Lcnt += 1
            if (Rcnt + Lcnt) % 2 == 0:
                ans[i] = Rcnt // 2 + Lcnt // 2
                ans[i + 1] = Rcnt // 2 + Lcnt // 2
            else:
                if Rcnt % 2 == 1:
                    ans[i] = Rcnt // 2 + Lcnt // 2 + 1
                    ans[i + 1] = Rcnt // 2 + Lcnt // 2
                else:
                    ans[i] = Rcnt // 2 + Lcnt // 2
                    ans[i + 1] = Rcnt // 2 + Lcnt // 2 + 1
    print(*ans)

=======
Suggestion 2

def main():
    s = input()
    l = len(s)
    ans = [0 for i in range(l)]
    cnt = 0
    flag = False
    for i in range(l):
        if s[i] == 'R':
            cnt += 1
            flag = False
        else:
            if flag:
                cnt += 1
            else:
                ans[i] += cnt//2
                ans[i-1] += cnt//2
                if cnt % 2 == 1:
                    ans[i-1] += 1
                    flag = True
                cnt = 0
    cnt = 0
    flag = False
    for i in range(l-1, -1, -1):
        if s[i] == 'L':
            cnt += 1
            flag = False
        else:
            if flag:
                cnt += 1
            else:
                ans[i] += cnt//2
                ans[i+1] += cnt//2
                if cnt % 2 == 1:
                    ans[i+1] += 1
                    flag = True
                cnt = 0
    print(*ans)

=======
Suggestion 3

def main():
    s = input()
    n = len(s)
    ans = [0]*n
    cnt = 0
    for i in range(n):
        if s[i] == 'R':
            cnt += 1
        else:
            ans[i] += cnt//2
            ans[i-1] += (cnt+1)//2
            cnt = 0
    cnt = 0
    for i in range(n-1,-1,-1):
        if s[i] == 'L':
            cnt += 1
        else:
            ans[i] += cnt//2
            ans[i+1] += (cnt+1)//2
            cnt = 0
    print(*ans)

=======
Suggestion 4

def main():
    s = input()
    n = len(s)
    ans = [0] * n
    flag = 0
    for i in range(n):
        if s[i] == 'R':
            flag += 1
        else:
            if flag % 2 == 0:
                ans[flag] += 1
            else:
                ans[flag - 1] += 1
            flag = 0
    flag = 0
    for i in range(n - 1, -1, -1):
        if s[i] == 'L':
            flag += 1
        else:
            if flag % 2 == 0:
                ans[n - 1 - flag] += 1
            else:
                ans[n - flag] += 1
            flag = 0
    print(*ans)

=======
Suggestion 5

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    cnt = 1
    for i in range(N-1):
        if S[i] == "R" and S[i+1] == "L":
            ans[i] += cnt//2
            ans[i+1] += cnt//2
            cnt = 1
        elif S[i] == "R" and S[i+1] == "R":
            cnt += 1
        elif S[i] == "L" and S[i+1] == "L":
            cnt += 1
        else:
            ans[i] += cnt//2
            ans[i+1] += cnt//2
            cnt = 1
    print(*ans)

=======
Suggestion 6

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    for i in range(N):
        if S[i] == "R":
            ans[i + 1] += 1
        else:
            ans[i] += 1
    ans = list(map(str, ans))
    print(" ".join(ans))

=======
Suggestion 7

def main():
    s = input()
    n = len(s)
    ans = [0]*n
    for i in range(n):
        if s[i] == "R":
            if s[i+1] == "R":
                ans[i+2] += ans[i]
                ans[i] = 0
            else:
                ans[i+1] += ans[i]
                ans[i] = 0
        else:
            if s[i-1] == "L":
                ans[i-2] += ans[i]
                ans[i] = 0
            else:
                ans[i-1] += ans[i]
                ans[i] = 0
    print(*ans)

=======
Suggestion 8

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    cnt = 0
    for i in range(N):
        if S[i] == 'R':
            cnt += 1
        else:
            ans[i] += cnt // 2
            ans[i-1] += (cnt + 1) // 2
            cnt = 0
    cnt = 0
    for i in range(N-1, -1, -1):
        if S[i] == 'L':
            cnt += 1
        else:
            ans[i] += cnt // 2
            ans[i+1] += (cnt + 1) // 2
            cnt = 0
    print(*ans, sep=' ')

=======
Suggestion 9

def main():
    s = input()
    n = len(s)
    ans = [0] * n
    for i in range(n):
        if s[i] == 'R':
            ans[i + 1] += 1
        else:
            ans[i - 1] += 1
    for i in range(n):
        print(ans[i], end=' ')
    print()

=======
Suggestion 10

def solve():
    # ++++ INPUT ++++
    S = input()
    N = len(S)
    # ++++ SOLVE ++++
    ans = [0] * N
    # R の位置を記録
    R = []
    for i in range(N):
        if S[i] == 'R':
            R.append(i)
    # R の位置を元に、各マスの人数を計算
    for i in range(N):
        # R の位置より左にある L の数
        # R の位置より右にある R の数
        # R の位置より右にある L の数
        # R の位置より左にある R の数
        r1 = len([r for r in R if r < i])
        r2 = len([r for r in R if r > i])
        l1 = i - r1
        l2 = N - i - r2
        # L から R に移動する人数
        if S[i] == 'L':
            ans[i - 1] += l1
            ans[i] += l2
        # R から L に移動する人数
        else:
            ans[i] += r1
            ans[i - 1] += r2
    # ++++ OUTPUT ++++
    print(*ans)
