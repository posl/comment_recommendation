Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = [input() for i in range(n)]
    print(max(set(s), key=s.count))

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
    n = int(input())
    votes = []
    for i in range(n):
        votes.append(input())
    print(max(votes, key=votes.count))

=======
Suggestion 4

def main():
    #input
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    #process
    D = {}
    for i in range(N):
        if S[i] in D:
            D[S[i]] += 1
        else:
            D[S[i]] = 1
    #output
    print(max(D, key=D.get))

=======
Suggestion 5

def get_max_vote_name():
    n = int(input())
    vote_dict = {}
    for i in range(n):
        name = input()
        if name in vote_dict:
            vote_dict[name] += 1
        else:
            vote_dict[name] = 1

    max_vote = 0
    max_name = ''
    for k, v in vote_dict.items():
        if v > max_vote:
            max_vote = v
            max_name = k
    print(max_name)

get_max_vote_name()

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    print(s[-1])

=======
Suggestion 7

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    names.sort()
    max = 0
    max_name = ""
    for name in names:
        if names.count(name) > max:
            max = names.count(name)
            max_name = name
    print(max_name)

=======
Suggestion 8

def main():
    #input
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    #process
    s.sort()
    c = {}
    for i in range(n):
        if s[i] in c:
            c[s[i]] += 1
        else:
            c[s[i]] = 1
    #output
    print(max(c, key=c.get))

=======
Suggestion 9

def main():
    n = int(input())
    votes = {}
    for i in range(n):
        s = input()
        if s not in votes:
            votes[s] = 1
        else:
            votes[s] += 1
    print(max(votes, key=votes.get))
