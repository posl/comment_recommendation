Synthesizing 10/10 solutions (Duplicates hidden)

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
    N = int(input())
    S = set()
    for i in range(N):
        S.add(input())
    print(len(S))

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

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s = set(s)
    print(len(s))

=======
Suggestion 5

def solve():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    print(len(s))

=======
Suggestion 6

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())

    S.sort()
    cnt = 0
    for i in range(N):
        if i == 0:
            cnt += 1
        else:
            if S[i] != S[i - 1]:
                cnt += 1

    print(cnt)

main()

=======
Suggestion 7

def main():
    num = int(input())
    list = []
    for i in range(num):
        list.append(input())
    print(len(set(list)))

=======
Suggestion 8

def main():
    print(len(set([input() for i in range(int(input()))])))

=======
Suggestion 9

def count_kinds_of_items():
    N = int(input())
    items = set()
    for i in range(N):
        items.add(input())
    print(len(items))
