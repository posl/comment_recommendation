Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s, t = input().split()
    ans = ""
    for i in range(n):
        ans += s[i]
        ans += t[i]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S, T = input().split()
    ans = ''
    for i in range(N):
        ans += S[i]
        ans += T[i]
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    s, t = input().split()
    ans = ""
    for i in range(n):
        ans += s[i] + t[i]
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    S, T = input().split()
    ans = ''
    for i in range(N):
        ans += S[i] + T[i]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    S, T = input().split()
    ans = ""
    for i in range(N):
        ans = ans + S[i] + T[i]
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    s, t = input().split()
    print("".join([s[i]+t[i] for i in range(n)]))

=======
Suggestion 7

def main():
    n = int(input())
    s = input().split()
    for i in range(n):
        print(s[0][i] + s[1][i], end='')

=======
Suggestion 8

def main():
    #入力
    N = int(input())
    S, T = input().split()

    #出力
    print("".join(S[i] + T[i] for i in range(N)))
