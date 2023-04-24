Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    ans = 0
    for i in range(N):
        for j in range(10):
            if S[i][j] == '8':
                ans = max(ans, (i+j)%10)
                break
    print(ans+10)

=======
Suggestion 2

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(10):
        for j in range(N):
            if S[j][i] == '8':
                ans = max(ans, i + (10 - (j + 1) % 10) % 10)
                break
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(10):
        ans = max(ans, S.count(str(i)))
    print(ans * 10)

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for i in range(N)]
    ans = 0
    for i in range(10):
        ans = max(ans, S.count(str(i)))
    print(ans * 10)

=======
Suggestion 5

def main():
    N = int(input())
    S = [input() for i in range(N)]
    ans = 0
    for i in range(10):
        ans = max(ans, min([S[j].index(str(i)) for j in range(N)]))
    print(ans + 10)

=======
Suggestion 6

def main():
    N = int(input())
    S = [input() for _ in range(N)]

    ans = 0
    for i in range(10):
        ans = max(ans, min([S[j].index(str(i)) for j in range(N)]))
    print(ans+N*10)

=======
Suggestion 7

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(10):
        ans = max(ans, min(s.count(s[j][i]) for j in range(n)))
    print(n * 10 - ans)

=======
Suggestion 8

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print(10 * (N - 1) + min(S[0].index(s) for s in S[0]))

=======
Suggestion 9

def main():
    N = int(input())
    S = [str(input()) for n in range(N)]
    ans = 0
    for i in range(10):
        t = 0
        for s in S:
            if s[i] != s[(i + 1) % 10]:
                t = max(t, i + 1)
        ans = max(ans, t)
    print(ans)
    return

=======
Suggestion 10

def main():
    N = int(input())
    reels = [input() for _ in range(N)]
    # 10個のリールに対して、最初の文字が何秒で表示されるかを計算する
    # 0秒目に表示される文字は、0秒目に押されるボタンの次の文字
    # 1秒目に表示される文字は、1秒目に押されるボタンの次の文字
    # ...
    # 9秒目に表示される文字は、9秒目に押されるボタンの次の文字
    # 10秒目に表示される文字は、0秒目に押されるボタンの次の文字
    # 11秒目に表示される文字は、1秒目に押されるボタンの次の文字
    # ...
    # 19秒目に表示される文字は、9秒目に押されるボタンの次の文字
    # でも、10秒目に表示される文字は、0秒目に押されるボタンの次の文字
    # ということで、10秒目に表示される文字は、(0 + 10) % 10 文字目
    # 11秒目に表示される文字は、(1 + 10) % 10 文字目
    # ...
    # 19秒目に表示される文字は、(9 + 10) % 10 文字目
    # ということで、10秒目に表示される文字は、(0 + 10) % 10 文字目
    # 11秒目に表示される文字は、(1 + 10) % 10 文字目
    # ...
    # 19秒目に表示される文字は、(9 + 10) % 10 文字目
    # ということで、10秒目に表示される文字は、(0 + 10) % 10 文字目
    # 11秒目に表示される文字は、(1 + 10) % 10 文字目
