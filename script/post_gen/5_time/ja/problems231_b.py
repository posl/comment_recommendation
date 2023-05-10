Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    votes = []
    for i in range(n):
        votes.append(input())
    print(max(votes, key=votes.count))

=======
Suggestion 2

def solve():
    # +++ input +++
    n = int(input())
    s = [input() for _ in range(n)]

    # +++ solve +++
    # 1. dict
    d = {}
    for i in range(n):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    # 2. list
    # d = []
    # for i in range(n):
    #     d.append(s[i])
    # 3. Counter
    # d = Counter(s)
    # 4. defaultdict
    # d = defaultdict(int)
    # for i in range(n):
    #     d[s[i]] += 1
    # 5. Counter + max
    # d = Counter(s)
    # d = max(d, key=d.get)
    # 6. Counter + most_common
    # d = Counter(s)
    # d = d.most_common(1)[0][0]

    # +++ output +++
    print(max(d, key=d.get))

=======
Suggestion 3

def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.sort()
    #print(S)
    import itertools
    max = 0
    ans = ""
    for i in itertools.groupby(S):
        #print(i)
        #print(list(i[1]))
        if max < len(list(i[1])):
            max = len(list(i[1]))
            ans = i[0]
    print(ans)
main()

=======
Suggestion 4

def solve():
    n = int(input())
    s = [input() for _ in range(n)]
    print(max(s, key=s.count))

=======
Suggestion 5

def main():
    n = int(input())
    s = [input() for i in range(n)]
    print(max(s,key=s.count))

=======
Suggestion 6

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    S.append("")
    max = 0
    max_name = ""
    now = 0
    for i in range(N):
        if S[i] == S[i+1]:
            now += 1
        else:
            if now > max:
                max = now
                max_name = S[i]
            now = 0
    print(max_name)

=======
Suggestion 7

def main():
    N = int(input())
    S = [input() for i in range(N)]
    print(max(S, key=S.count))

=======
Suggestion 8

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print(max(s, key=s.count))
