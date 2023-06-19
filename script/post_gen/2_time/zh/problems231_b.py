Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = {}
    for i in range(n):
        name = input()
        if name in s:
            s[name] += 1
        else:
            s[name] = 1
    print(max(s, key=s.get))

=======
Suggestion 2

def solution():
    N = int(input())
    name = input()
    name_list = []
    name_list.append(name)
    for i in range(1, N):
        name = input()
        name_list.append(name)
    print(max(name_list, key=name_list.count))

=======
Suggestion 3

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    print(S[-1])

=======
Suggestion 4

def main():
    n = int(input())
    max = 0
    max_name = ''
    dic = {}
    for i in range(n):
        name = input()
        if name in dic:
            dic[name] += 1
        else:
            dic[name] = 1
        if dic[name] > max:
            max = dic[name]
            max_name = name
    print(max_name)

=======
Suggestion 5

def main():
    n = int(input())
    candidates = {}
    max_vote = 0
    max_candidate = ""
    for i in range(n):
        candidate = input()
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1
        if candidates[candidate] > max_vote:
            max_vote = candidates[candidate]
            max_candidate = candidate
    print(max_candidate)

=======
Suggestion 6

def get_max_vote_name():
    n = int(input())
    name_list = []
    vote_list = []
    for i in range(n):
        name = input()
        if name not in name_list:
            name_list.append(name)
            vote_list.append(1)
        else:
            vote_list[name_list.index(name)] += 1
    return name_list[vote_list.index(max(vote_list))]

=======
Suggestion 7

def get_max_vote_name(names):
    max_vote_name = ""
    max_vote_count = 0
    for name in names:
        vote_count = names.count(name)
        if vote_count > max_vote_count:
            max_vote_count = vote_count
            max_vote_name = name
    return max_vote_name

=======
Suggestion 8

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    print(s[-1])

=======
Suggestion 9

def get_max_name(names):
    max_name = ""
    max_count = 0
    for name in names:
        if names.count(name) > max_count:
            max_count = names.count(name)
            max_name = name
    return max_name
