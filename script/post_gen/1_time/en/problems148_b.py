Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S, T = input().split()
    ans = ""
    for i in range(N):
        ans += S[i] + T[i]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S, T = input().split()
    result = ""
    for i in range(N):
        result += S[i] + T[i]
    print(result)

=======
Suggestion 3

def main():
    N = int(input())
    S, T = input().split()
    for i in range(N):
        print(S[i], end="")
        print(T[i], end="")
    print()

=======
Suggestion 4

def main():
    N = int(input())
    S, T = input().split()
    for i in range(N):
        print(S[i], T[i], sep='', end='')
    print()

=======
Suggestion 5

def main():
    n = int(input())
    s, t = input().split()
    print(''.join([s[i] + t[i] for i in range(n)]))

=======
Suggestion 6

def main():
    N = int(input())
    S, T = input().split()
    print(''.join([S[i] + T[i] for i in range(N)]))

=======
Suggestion 7

def main():
    n = int(input())
    s, t = input().split()
    print("".join(s[i] + t[i] for i in range(n)))

main()

=======
Suggestion 8

def main():
    N = int(input())
    S, T = input().split()
    print(''.join(S[i] + T[i] for i in range(N)))

=======
Suggestion 9

def main():
    n = int(input())
    s, t = input().split()
    for i in range(n):
        print(s[i], t[i], end='')
    print()

=======
Suggestion 10

def main():
    n = int(input())
    s, t = input().split()
    print("".join([s[i]+t[i] for i in range(n)]))
