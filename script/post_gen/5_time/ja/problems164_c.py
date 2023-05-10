Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    s.append('dummy')
    cnt = 0
    for i in range(n):
        if s[i] != s[i+1]:
            cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print(len(set(s)))

=======
Suggestion 3

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print(len(set(s)))

=======
Suggestion 4

def problem164_c():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print(len(set(s)))
