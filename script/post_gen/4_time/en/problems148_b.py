Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S, T = input().split()
    ans = ''
    for i in range(N):
        ans += S[i]
        ans += T[i]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S, T = input().split()
    ans = ''
    for i in range(N):
        ans += S[i] + T[i]
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    s, t = input().split()
    result = ''
    for i in range(n):
        result += s[i] + t[i]
    print(result)

=======
Suggestion 4

def main():
    N = int(input())
    S, T = input().split()
    result = ''
    for i in range(N):
        result += S[i] + T[i]
    print(result)

=======
Suggestion 5

def main():
    N = int(input())
    S, T = input().split()

    ans = []
    for i in range(N):
        ans.append(S[i])
        ans.append(T[i])

    print(''.join(ans))

=======
Suggestion 6

def main():
    n = int(input())
    s, t = input().split(' ')
    result = ''
    for i in range(n):
        result += s[i] + t[i]
    print(result)

=======
Suggestion 7

def main():
    n = int(input())
    s, t = input().split()
    print("".join([s[i]+t[i] for i in range(n)]))
