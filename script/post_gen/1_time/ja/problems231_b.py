Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    candidates = {}
    for i in range(n):
        name = input()
        if name in candidates:
            candidates[name] += 1
        else:
            candidates[name] = 1
    #print(candidates)
    max_vote = max(candidates.values())
    #print(max_vote)
    for key, value in candidates.items():
        if value == max_vote:
            print(key)

=======
Suggestion 2

def main():
    N = int(input())
    S = [input() for i in range(N)]
    count = {}
    for s in S:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
    print(max(count, key=lambda x: count[x]))

=======
Suggestion 3

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S_set = set(S)
    S_count = []
    for i in S_set:
        S_count.append(S.count(i))
    print(S[S_count.index(max(S_count))])

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print(max(S, key=S.count))

=======
Suggestion 5

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    C = Counter(S)
    print(C.most_common(1)[0][0])

=======
Suggestion 6

def main():
    N = int(input())
    S = [input() for i in range(N)]
    S = sorted(S)
    S = sorted(S, key=S.count, reverse=True)
    print(S[0])

=======
Suggestion 7

def main():
    N = int(input())
    cands = []
    for i in range(N):
        cands.append(input())
    print(max(cands, key=cands.count))

=======
Suggestion 8

def main():
    n = int(input())
    s = [input() for i in range(n)]
    s_set = set(s)
    max_vote = 0
    winner = ""
    for name in s_set:
        if max_vote < s.count(name):
            max_vote = s.count(name)
            winner = name
    print(winner)

=======
Suggestion 9

def main():
    N = int(input())
    votes = [input() for _ in range(N)]
    votes.sort()
    count = 1
    max_count = 0
    max_count_name = ""
    for i in range(1, N):
        if votes[i] == votes[i-1]:
            count += 1
        else:
            if count > max_count:
                max_count = count
                max_count_name = votes[i-1]
            count = 1
    if count > max_count:
        max_count = count
        max_count_name = votes[-1]
    print(max_count_name)

=======
Suggestion 10

def main():
    #入力
    N = int(input())
    S = [input() for i in range(N)]
    #辞書型にして集計
    D = {}
    for i in range(N):
        if S[i] in D:
            D[S[i]] += 1
        else:
            D[S[i]] = 1
    #最大値を求める
    max = 0
    for i in D.values():
        if i > max:
            max = i
    #最大値と一致するものを表示
    for i in D.keys():
        if D[i] == max:
            print(i)
