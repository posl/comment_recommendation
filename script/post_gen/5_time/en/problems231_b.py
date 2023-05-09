Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    d={}
    for i in range(n):
        s = input()
        if s in d.keys():
            d[s] += 1
        else:
            d[s] = 1
    print(max(d, key=d.get))

=======
Suggestion 2

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    print(max(set(S), key = S.count))

=======
Suggestion 3

def main():
    N = int(input())
    S = [input() for i in range(N)]
    print(max(set(S), key=S.count))

=======
Suggestion 4

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print(max(s, key=s.count))

=======
Suggestion 5

def main():
    n = int(input())
    list = []
    for i in range(n):
        list.append(input())
    d = {}
    for i in list:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print(max(d, key=d.get))

=======
Suggestion 6

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print(max(s, key=s.count))

=======
Suggestion 7

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    count = 0
    max_count = 0
    max_name = S[0]
    for i in range(N):
        if S[i] == max_name:
            count += 1
        else:
            if count > max_count:
                max_count = count
                max_name = S[i-1]
            count = 1
    if count > max_count:
        max_count = count
        max_name = S[N-1]
    print(max_name)

=======
Suggestion 8

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    s.reverse()
    print(s[0])

=======
Suggestion 9

def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    print(max(set(S), key = S.count))

=======
Suggestion 10

def main():
    # get input
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    #print(s)
    # find the most votes
    max_vote = 0
    max_name = ""
    for name in s:
        if s.count(name) > max_vote:
            max_vote = s.count(name)
            max_name = name
    #print(max_vote)
    #print(max_name)
    # print the name
    print(max_name)
