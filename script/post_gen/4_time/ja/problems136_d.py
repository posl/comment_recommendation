Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    n = len(s)
    ans = [0] * n
    cnt = 0
    for i in range(n):
        if s[i] == 'R':
            cnt += 1
        else:
            ans[i] += cnt // 2
            ans[i - 1] += cnt - cnt // 2
            cnt = 0
    cnt = 0
    for i in range(n - 1, -1, -1):
        if s[i] == 'L':
            cnt += 1
        else:
            ans[i] += cnt // 2
            ans[i + 1] += cnt - cnt // 2
            cnt = 0
    print(*ans)

=======
Suggestion 2

def main():
    S = input()
    N = len(S)
    L = []
    R = []
    for i in range(N):
        if S[i] == 'L':
            L.append(i)
        else:
            R.append(i)
    ans = [0] * N
    for i in R:
        if (i - L[0]) % 2 == 0:
            ans[L[0]] += 1
        else:
            ans[L[0] - 1] += 1
    for i in L:
        if (R[-1] - i) % 2 == 0:
            ans[R[-1]] += 1
        else:
            ans[R[-1] + 1] += 1
    for i in range(len(L) - 1):
        if (L[i + 1] - L[i]) % 2 == 0:
            ans[L[i + 1]] += 1
        else:
            ans[L[i + 1] - 1] += 1
    for i in range(len(R) - 1):
        if (R[i + 1] - R[i]) % 2 == 0:
            ans[R[i + 1]] += 1
        else:
            ans[R[i + 1] + 1] += 1
    print(" ".join(map(str, ans)))

=======
Suggestion 3

def main():
    s = input()
    n = len(s)
    ans = [0] * n
    for i in range(n):
        if s[i] == "R":
            ans[i+1] += 1
        else:
            ans[i] += 1
    for i in range(10**100):
        tmp = [0] * n
        for j in range(n):
            if s[j] == "R":
                tmp[j+1] += ans[j]
            else:
                tmp[j] += ans[j]
        ans = tmp
    print(*ans)

=======
Suggestion 4

def solve():
    s = input()
    n = len(s)
    ans = [0]*n
    l = 0
    r = 0
    for i in range(n):
        if s[i] == 'L':
            r = i
        else:
            l = i
        if s[i] == 'L':
            ans[r] += 1
        else:
            ans[l] += 1
    print(*ans)

=======
Suggestion 5

def main():
    # input
    S = input()
    N = len(S)
    # compute
    ans = [0] * N
    for i in range(N):
        if S[i] == "R":
            if i % 2 == 0:
                ans[i+1] += 1
            else:
                ans[i-1] += 1
        else:
            if i % 2 == 0:
                ans[i-1] += 1
            else:
                ans[i+1] += 1
    # output
    print(*ans)

=======
Suggestion 6

def main():
    s = input()
    n = len(s)
    #print(s)
    #print(n)
    a = [0] * n
    #print(a)
    for i in range(n):
        if s[i] == "R":
            a[i+1] += 1
        else:
            a[i] += 1
    #print(a)
    for i in range(10**100):
        b = [0] * n
        for j in range(n):
            if a[j] % 2 == 1:
                b[j-1] += 1
            else:
                b[j+1] += 1
        a = b
    print(*a)

=======
Suggestion 7

def main():
    # データ入力
    S = input()
    # 計算
    N = len(S)
    ans = [0] * N
    for i in range(N):
        if S[i] == 'R':
            if S[i + 1] == 'R':
                ans[i + 2] += ans[i] + 1
                ans[i] = 0
            else:
                ans[i + 1] += ans[i] + 1
                ans[i] = 0
        else:
            if S[i - 1] == 'L':
                ans[i - 2] += ans[i] + 1
                ans[i] = 0
            else:
                ans[i - 1] += ans[i] + 1
                ans[i] = 0
    # データ出力
    print(' '.join(map(str, ans)))
    return

=======
Suggestion 8

def main():
    s = input()
    l = len(s)
    rl = [0] * l
    rr = [0] * l
    for i in range(0, l):
        if s[i] == 'R':
            rl[i] += 1
            rr[i - 1] += 1
        else:
            rr[i] += 1
            rl[i + 1] += 1
    ans = []
    for i in range(0, l):
        ans.append(str(rl[i] + rr[i]))
    print(' '.join(ans))

=======
Suggestion 9

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    # Rがある場所を探す
    R_index = []
    for i in range(N):
        if S[i] == 'R':
            R_index.append(i)
    # Rがない場合
    if len(R_index) == 0:
        for i in range(N):
            ans[i] = N
    # Rがある場合
    else:
        for i in range(N):
            # Rの左端の場合
            if i == 0:
                # 1回の移動で右に行く
                ans[R_index[0]] += 1
            # Rの右端の場合
            elif i == N - 1:
                # 1回の移動で左に行く
                ans[R_index[-1]] += 1
            # Rの間の場合
            else:
                # Rの左端にいる場合
                if S[i] == 'R':
                    # 1回の移動で右に行く
                    ans[R_index[0]] += 1
                    # 1回の移動で左に行く
                    ans[R_index[0] - 1] += 1
                # Rの右端にいる場合
                elif S[i] == 'L':
                    # 1回の移動で左に行く
                    ans[R_index[-1]] += 1
                    # 1回の移動で右に行く
                    ans[R_index[-1] + 1] += 1
    print(*ans)
