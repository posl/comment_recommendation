Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N // 2):
        if S[i] != S[N - i - 1]:
            ans += min(A, B)
    print(ans)

=======
Suggestion 2

def main():
    n, a, b = map(int, input().split())
    s = input()
    ans = 0
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            ans += b
    print(min(ans, (n - 1) * a))

=======
Suggestion 3

def main():
    n, a, b = map(int, input().split())
    s = input()
    ans = 0
    for i in range(n//2):
        if s[i] != s[-(i+1)]:
            ans += b
    if n%2==1:
        if s[n//2] != s[-(n//2+1)]:
            ans += b
    if ans == 0:
        print(0)
    else:
        print(ans+a)

=======
Suggestion 4

def main():
    N, A, B = map(int, input().split())
    S = input()
    ans = 0
    if S == S[::-1]:
        print(ans)
        return
    for i in range(N//2):
        if S[i] != S[N-1-i]:
            ans += min(A, B)
    print(ans)

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())
    S = input()
    S = S + S
    ans = 0
    for i in range(N):
        if S[i] == S[i + N - 1]:
            continue
        else:
            ans += B
    print(ans)

=======
Suggestion 6

def main():
    # 入力
    N, A, B = map(int, input().split())
    S = input()
    # 処理
    ans = 0
    for i in range(N):
        if S[i] == S[N-i-1]:
            continue
        else:
            ans += min(A, B)
    # 出力
    print(ans)

=======
Suggestion 7

def main():
    N, A, B = map(int, input().split())
    S = input()
    #S = "rrefa"
    #A = 1
    #B = 2
    #S = "bcdfcgaa"
    #A = 10**9
    #B = 10**9

    #文字列が回文かどうか判定する関数
    def is_palindrome(s):
        return s == s[::-1]

    #文字列を左に1つずつずらす関数
    def shift(s):
        return s[1:] + s[0]

    #文字列を回文にするために必要なコストを計算する関数
    def cost(s):
        #文字列が回文なら0を返す
        if is_palindrome(s):
            return 0
        #文字列の左端と右端が同じなら文字列を左に1つずつずらして再帰的にコストを計算する
        if s[0] == s[-1]:
            return cost(s[1:-1])
        #文字列の左端と右端が異なるなら文字列を左に1つずつずらして再帰的にコストを計算し、その結果にBを足す
        else:
            return cost(s[1:-1]) + B

    #文字列を回文にするために必要なコストを計算する
    c = cost(S)

    #文字列を回文にするために必要なコストがAより小さいならAを出力する
    if c < A:
        print(A)
    #文字列を回文にするために必要なコストがAより大きいなら文字列を左に1つずつずらして回文になるまで繰り返す
    else:
        #文字列を回文にするために必要なコストを計算する
        c = cost(S)
        #文字列を回文にするために必要なコストがA

=======
Suggestion 8

def main():
    N, A, B = map(int, input().split())
    S = input()
    S = list(S)
    S2 = S[:]
    S2.reverse()
    if S == S2:
        print(0)
        return
    count = 0
    for i in range(N):
        if S[i] == S2[i]:
            count += 1
        else:
            break
    if count == N:
        print(0)
        return
    if count == N-2:
        print(min(A, B))
        return
    if count == N-1:
        print(B)
        return
    print(min(A, B)*count + B)

main()

=======
Suggestion 9

def main():
    N, A, B = map(int, input().split())
    S = input()
    if A <= B:
        print(A * (N - 1))
        return
    ans = 0
    for i in range(N - 1):
        if S[i] != S[i + 1]:
            ans += B
        else:
            ans += A
    print(ans)

=======
Suggestion 10

def is_palindrome(s):
    return s == s[::-1]
