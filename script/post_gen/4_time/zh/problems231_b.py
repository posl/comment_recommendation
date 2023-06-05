Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    votes = {}
    for i in range(n):
        name = input()
        if name in votes:
            votes[name] = votes[name] + 1
        else:
            votes[name] = 1
    max = 0
    max_name = ""
    for k in votes:
        if votes[k] > max:
            max = votes[k]
            max_name = k
    print(max_name)

=======
Suggestion 2

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print(max(s, key=s.count))

=======
Suggestion 3

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    print(max(set(S), key=S.count))

=======
Suggestion 4

def main():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    print(max(d, key=d.get))

=======
Suggestion 5

def main():
    num = int(input())
    dic = {}
    for i in range(num):
        name = input()
        if name in dic:
            dic[name] += 1
        else:
            dic[name] = 1
    max = 0
    for i in dic:
        if dic[i] > max:
            max = dic[i]
            max_name = i
    print(max_name)

=======
Suggestion 6

def solution():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    print(max(d, key=d.get))

=======
Suggestion 7

def main():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    print(max(d, key=d.get))
main()

=======
Suggestion 8

def solve():
    N = int(input())
    d = {}
    for i in range(N):
        S = input()
        if S not in d:
            d[S] = 0
        d[S] += 1
    #print(d)
    print(max(d, key=d.get))
    return 0

=======
Suggestion 9

def main():
    N = int(input())
    S = [input() for i in range(N)]
    print(max(S, key=S.count))
