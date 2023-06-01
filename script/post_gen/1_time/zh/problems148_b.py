Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s, t = input().split()
    result = ''
    for i in range(n):
        result += s[i]
        result += t[i]
    print(result)

=======
Suggestion 2

def main():
    n = int(input())
    s, t = map(str, input().split())
    ans = ''
    for i in range(n):
        ans += s[i] + t[i]
    print(ans)

=======
Suggestion 3

def getStr():
    n = int(input())
    s = input()
    t = input()
    result = ""
    for i in range(n):
        result += s[i]
        result += t[i]
    print(result)

=======
Suggestion 4

def problems148_b():
    n = int(input())
    s, t = input().split()

    result = ""
    for i in range(n):
        result += s[i] + t[i]

    print(result)

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
    # N = int(input())
    # s, t = input().split()
    N = 8
    s = "hmhmnknk"
    t = "uuuuuuuu"
    result = ""
    for i in range(N):
        result += s[i] + t[i]
    print(result)

=======
Suggestion 7

def main():
    n = int(input())
    s, t = input().split()
    result = ""
    for i in range(n):
        result += s[i] + t[i]
    print(result)

main()

=======
Suggestion 8

def problem148_b():
    n = int(input())
    s, t = input().split()
    res = ""
    for i in range(n):
        res += s[i] + t[i]
    print(res)

=======
Suggestion 9

def main():
    n = int(input())
    s, t = input().split()
    result = ''
    for i in range(n):
        result += s[i] + t[i]
    print(result)
