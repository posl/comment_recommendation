Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print(len(set(s)))

=======
Suggestion 2

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print(len(set(s)))
main()

=======
Suggestion 3

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    print(len(set(S)))

=======
Suggestion 4

def count_num():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    num = 1
    for i in range(N-1):
        if S[i] != S[i+1]:
            num += 1
    print(num)

=======
Suggestion 5

def main():
    n = int(input())
    s = [input() for i in range(n)]
    print(len(set(s)))

=======
Suggestion 6

def solve():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    print(len(s))

=======
Suggestion 7

def get_input():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    return n, s

=======
Suggestion 8

def main():
    n = int(input())
    s = set()
    for _ in range(n):
        s.add(input())
    print(len(s))

main()

=======
Suggestion 9

def main():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    print(len(s))

=======
Suggestion 10

def problems164_c():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    ans = 0
    for i in range(n):
        if i == 0 or s[i] != s[i-1]:
            ans += 1
    print(ans)
