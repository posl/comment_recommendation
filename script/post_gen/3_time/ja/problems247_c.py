Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def s(n):
    if n == 1:
        return [1]
    else:
        return s(n-1) + [n] + s(n-1)

=======
Suggestion 2

def s(n):
    if n == 1:
        return [1]
    return s(n-1) + [n] + s(n-1)

=======
Suggestion 3

def make_s(n):
    if n == 1:
        return [1]
    else:
        return make_s(n-1) + [n] + make_s(n-1)

n = int(input())
print(" ".join(map(str,make_s(n))))

=======
Suggestion 4

def s(n):
    if n==1:
        return [1]
    else:
        return s(n-1)+[n]+s(n-1)

n=int(input())
print(' '.join(map(str,s(n))))

=======
Suggestion 5

def solve(N):
    if N == 1:
        return [1]
    else:
        return solve(N-1) + [N] + solve(N-1)

N = int(input())
print(*solve(N))

=======
Suggestion 6

def solve():
    N = int(input())
    ans = []
    def f(N):
        if N == 1:
            ans.append(1)
            return
        f(N-1)
        ans.append(N)
        f(N-1)
    f(N)
    print(*ans)
solve()

=======
Suggestion 7

def main():
    N = int(input())
    s = [1]
    for i in range(2,N+1):
        s = s + [i] + s
    print(*s)

=======
Suggestion 8

def dfs(n, s):
    if n == 0:
        return s
    return dfs(n - 1, s + [n] + s)

=======
Suggestion 9

def main():
    # 入力
    N = int(input())
    # N=1の時の例外処理
    if N == 1:
        print(1)
        return
    # リストの作成
    s = [1]
    # 処理
    for i in range(2, N + 1):
        s.append(i)
        s.extend(s)
    # 出力
    print(*s)
