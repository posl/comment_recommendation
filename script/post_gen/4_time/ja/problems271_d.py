Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, S = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # dp[i][j] = i枚目までのカードを使ってjを作れるか
    dp = [[False]*(S+1) for _ in range(N+1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S+1):
            if j >= A[i]:
                dp[i+1][j] = dp[i+1][j] or dp[i][j-A[i]]
            if j >= B[i]:
                dp[i+1][j] = dp[i+1][j] or dp[i][j-B[i]]

    if not dp[N][S]:
        print("No")
        return

    ans = ""
    i = N
    j = S
    while i > 0:
        if j >= A[i-1] and dp[i-1][j-A[i-1]]:
            ans = "H" + ans
            j -= A[i-1]
        else:
            ans = "T" + ans
            j -= B[i-1]
        i -= 1
    print("Yes")
    print(ans)

=======
Suggestion 2

def solve():
    N, S = map(int, input().split())
    A = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append((a, b))

    for i in range(1 << N):
        sum = 0
        for j in range(N):
            if (i & (1 << j)) != 0:
                sum += A[j][0]
            else:
                sum += A[j][1]
        if sum == S:
            print("Yes")
            for j in range(N):
                if (i & (1 << j)) != 0:
                    print("H", end="")
                else:
                    print("T", end="")
            print()
            return
    print("No")

=======
Suggestion 3

def dfs(i, sum):
    if i == n:
        if sum == s:
            return True
        else:
            return False
    if dfs(i + 1, sum + a[i]):
        b[i] = 1
        return True
    if dfs(i + 1, sum):
        b[i] = 0
        return True
    return False

n, s = map(int, input().split())
a = []
b = [0] * n
for i in range(n):
    a.append(list(map(int, input().split())))

=======
Suggestion 4

def main():
    n, s = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ans = []
    for i in range(2**n):
        tmp = []
        for j in range(n):
            if (i >> j) & 1:
                tmp.append(ab[j][1])
            else:
                tmp.append(ab[j][0])
        if sum(tmp) == s:
            ans = tmp
            break
    if ans:
        print("Yes")
        for i in ans:
            print("T" if i == ab[ans.index(i)][1] else "H", end="")
        print()
    else:
        print("No")

=======
Suggestion 5

def main():
    import sys
    readline = sys.stdin.buffer.readline

    N, S = map(int, readline().split())
    AB = [list(map(int, readline().split())) for _ in range(N)]

    #print(N, S)
    #print(AB)

    #dp[i][s] = i枚目までのカードを見て、表をs枚選んだときの、裏の枚数の最小値
    #dp[i][s] = min(dp[i-1][s], dp[i-1][s-1]+1)
    #dp[i][s] = min(dp[i-1][s], dp[i-1][s-a[i]]+1)
    dp = [[float("inf")] * (S+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        a, b = AB[i]
        for s in range(S+1):
            if s >= a:
                dp[i+1][s] = min(dp[i][s], dp[i][s-a]+b)
            else:
                dp[i+1][s] = dp[i][s]

    #print(dp)
    if dp[N][S] == float("inf"):
        print("No")
    else:
        print("Yes")
        ans = []
        s = S
        for i in range(N-1, -1, -1):
            a, b = AB[i]
            if s >= a and dp[i][s-a] + b == dp[i+1][s]:
                ans.append("T")
                s -= a
            else:
                ans.append("H")
        print("".join(ans[::-1]))

=======
Suggestion 6

def main():
    # 入力
    n, s = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(n)]

    # 組み合わせを全探索
    for i in range(2**n):
        # 2進数で表す
        bit = format(i, 'b').zfill(n)
        # 表の合計値
        sum_t = 0
        # 裏の合計値
        sum_f = 0
        for j in range(n):
            # 1なら表
            if bit[j] == '1':
                sum_t += cards[j][0]
            # 0なら裏
            else:
                sum_f += cards[j][1]
        # 表の合計値と裏の合計値が等しければ終了
        if sum_t == s == sum_f:
            print('Yes')
            print(bit.replace('1', 'H').replace('0', 'T'))
            return
    # 組み合わせがなければNo
    print('No')

=======
Suggestion 7

def main():
    N, S = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(N)]

    # 1枚目のカードを表にするか裏にするかの組み合わせ
    for i in range(2):
        # 2枚目のカードを表にするか裏にするかの組み合わせ
        for j in range(2):
            # 3枚目のカードを表にするか裏にするかの組み合わせ
            for k in range(2):
                # 4枚目のカードを表にするか裏にするかの組み合わせ
                for l in range(2):
                    # 5枚目のカードを表にするか裏にするかの組み合わせ
                    for m in range(2):
                        sum = 0
                        if i == 0:
                            sum += cards[0][0]
                        else:
                            sum += cards[0][1]
                        if j == 0:
                            sum += cards[1][0]
                        else:
                            sum += cards[1][1]
                        if k == 0:
                            sum += cards[2][0]
                        else:
                            sum += cards[2][1]
                        if l == 0:
                            sum += cards[3][0]
                        else:
                            sum += cards[3][1]
                        if m == 0:
                            sum += cards[4][0]
                        else:
                            sum += cards[4][1]
                        if sum == S:
                            print('Yes')
                            if i == 0:
                                print('H', end='')
                            else:
                                print('T', end='')
                            if j == 0:
                                print('H', end='')
                            else:
                                print('T', end='')
                            if k == 0:
                                print('H', end='')
                            else:
                                print('T', end='')
                            if l == 0:
                                print('H', end='')
                            else:
                                print('T', end='')
                            if m == 0:
                                print('H')
                            else:
                                print('T')
                            exit()
    print('No')

=======
Suggestion 8

def main():
  N, S = map(int, input().split())
  cards = [list(map(int, input().split())) for _ in range(N)]
  for i in range(2 ** N):
    count = 0
    sum = 0
    ans = ""
    for j in range(N):
      if ((i >> j) & 1):
        count += 1
        sum += cards[j][0]
        ans += "H"
      else:
        sum += cards[j][1]
        ans += "T"
    if count == N and sum == S:
      print("Yes")
      print(ans)
      return
  print("No")
  return

=======
Suggestion 9

def cardgame(n, s, cards):
    for i in range(2**n):
        sum = 0
        result = ""
        for j in range(n):
            if (i >> j) & 1:
                sum += cards[j][0]
                result += "H"
            else:
                sum += cards[j][1]
                result += "T"
        if sum == s:
            return "Yes", result
    return "No", ""

=======
Suggestion 10

def solve(n, s, cards):
    # ここに処理を追記
    for i in range(2 ** n):
        sum = 0
        result = ""
        for j in range(n):
            if ((i >> j) & 1):
                sum += cards[j][1]
                result += "T"
            else:
                sum += cards[j][0]
                result += "H"
        if sum == s:
            return "Yes\n" + result
    return "No"

n, s = map(int, input().split())
cards = [list(map(int, input().split())) for i in range(n)]

print(solve(n, s, cards))
