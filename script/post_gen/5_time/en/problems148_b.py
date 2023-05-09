Synthesizing 10/10 solutions

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
    N = int(input())
    S, T = input().split()
    result = ""
    for i in range(N):
        result += S[i] + T[i]
    print(result)

=======
Suggestion 4

def main():
    n = int(input())
    s, t = input().split()
    result = []
    for i in range(n):
        result.append(s[i])
        result.append(t[i])
    print("".join(result))

=======
Suggestion 5

def main():
    n = int(input())
    s, t = input().split()

    ans = ''
    for i in range(n):
        ans += s[i] + t[i]

    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    S, T = input().split()

    result = ''
    for i in range(N):
        result += S[i] + T[i]
    print(result)

=======
Suggestion 7

def main():
    N = int(input())
    S,T = input().split()

    result = ""
    for i in range(N):
        result += S[i]
        result += T[i]

    print(result)

=======
Suggestion 8

def main():
    N = int(input())
    S, T = input().split()
    new_str = ''
    for i in range(N):
        new_str += (S[i] + T[i])
    print(new_str)

=======
Suggestion 9

def alternate_string(s, t):
    result = ''
    for i in range(len(s)):
        result += s[i]
        result += t[i]
    return result

=======
Suggestion 10

def alternate(s, t):
    result = ""
    for i in range(len(s)):
        result += s[i] + t[i]

    return result
