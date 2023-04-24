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
    print(S[:a-1] + S[b-1] + S[a:b-1] + S[a-1] + S[b:])

=======
Suggestion 3

def main():
    S = input()
    a, b = map(int, input().split())
    S = S[:a-1] + S[b-1] + S[a:b-1] + S[a-1] + S[b:]
    print(S)

=======
Suggestion 4

def main():
    S = input()
    a, b = map(int, input().split())
    S = list(S)
    S[a-1], S[b-1] = S[b-1], S[a-1]
    print(''.join(S))

=======
Suggestion 5

def main():
    s = input()
    a, b = map(int, input().split())
    s = list(s)
    s[a-1], s[b-1] = s[b-1], s[a-1]
    print(''.join(s))

=======
Suggestion 6

def main():
    S = input()
    a, b = map(int, input().split())
    S = list(S)
    S[a-1], S[b-1] = S[b-1], S[a-1]
    print("".join(S))
