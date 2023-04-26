Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    print(len(s))

=======
Suggestion 2

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    cnt = 1
    for i in range(N-1):
        if S[i] != S[i+1]:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print(len(set(s)))

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for i in range(N)]
    print(len(set(S)))

=======
Suggestion 5

def main():
    n = int(input())
    s = [input() for i in range(n)]
    print(len(set(s)))

=======
Suggestion 6

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())

    S.sort()
    count = 0
    for i in range(N):
        if i == 0:
            count += 1
        else:
            if S[i-1] != S[i]:
                count += 1

    print(count)

=======
Suggestion 7

def count_unique_items(items):
    unique_items = set(items)
    return len(unique_items)
