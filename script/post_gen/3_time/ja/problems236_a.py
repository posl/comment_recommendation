Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    a, b = map(int, input().split())
    print(s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:])

=======
Suggestion 2

def main():
    S = input()
    a, b = map(int, input().split())
    S = list(S)
    S[a - 1], S[b - 1] = S[b - 1], S[a - 1]
    print(''.join(S))

=======
Suggestion 3

def main():
    s = input()
    a, b = map(int, input().split())
    s = list(s)
    s[a-1], s[b-1] = s[b-1], s[a-1]
    print(''.join(s))

=======
Suggestion 4

def main():
    S = input()
    a, b = map(int, input().split())
    S = list(S)
    S[a-1], S[b-1] = S[b-1], S[a-1]
    print("".join(S))

=======
Suggestion 5

def main():
    S = list(input())
    a, b = map(int, input().split())
    S[a - 1], S[b - 1] = S[b - 1], S[a - 1]
    print(''.join(S))

=======
Suggestion 6

def main():
    S = input()
    a,b = map(int,input().split())
    S = list(S)
    S[a-1],S[b-1] = S[b-1],S[a-1]
    print("".join(S))

main()

=======
Suggestion 7

def main():
    S, a, b = input().split()
    a = int(a)
    b = int(b)
    S = list(S)
    S[a-1], S[b-1] = S[b-1], S[a-1]
    S = ''.join(S)
    print(S)
