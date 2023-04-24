Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    candidates = {}
    for i in range(n):
        s = input()
        if s in candidates:
            candidates[s] += 1
        else:
            candidates[s] = 1
    max_vote = max(candidates.values())
    for name, vote in candidates.items():
        if vote == max_vote:
            print(name)
            break

=======
Suggestion 2

def main():
    num = int(input())
    vote = {}
    for i in range(num):
        name = input()
        if name in vote:
            vote[name] += 1
        else:
            vote[name] = 1
    print(max(vote, key=vote.get))

=======
Suggestion 3

def main():
    N = int(input())
    S = [input() for _ in range(N)]

    max = 0
    for i in range(N):
        if S.count(S[i]) > max:
            max = S.count(S[i])
            name = S[i]

    print(name)

=======
Suggestion 4

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print(max(set(s), key=s.count))

=======
Suggestion 5

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print(max(s, key=s.count))

=======
Suggestion 6

def main():
    N = int(input())
    S = [input() for i in range(N)]
    print(max(S, key=S.count))

=======
Suggestion 7

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    max = 0
    max_name = ""
    name = ""
    for i in range(N):
        if name == S[i]:
            max += 1
        else:
            name = S[i]
            max = 1
        if max > max_name:
            max_name = name
    print(max_name)

=======
Suggestion 8

def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.sort()
    print(max(S, key=S.count))

=======
Suggestion 9

def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.sort()
    S_max = S.count(S[-1])
    for i in range(N):
        if S_max == S.count(S[i]):
            print(S[i])
