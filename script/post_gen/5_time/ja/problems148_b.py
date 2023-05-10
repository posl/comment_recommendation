Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S, T = input().split()

    ans = ""
    for i in range(N):
        ans += S[i]
        ans += T[i]
    print(ans)
main()

=======
Suggestion 2

def main():
    n = int(input())
    s, t = input().split()
    print(''.join([s[i]+t[i] for i in range(n)]))

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
    ans = ""
    for i in range(N):
        ans += S[i] + T[i]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    S, T = input().split()
    ans = ''
    for i in range(N):
        ans += S[i]
        ans += T[i]
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    s, t = input().split()
    ans = ''
    for i in range(n):
        ans += s[i] + t[i]
    print(ans)
