Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print(max(d, key=d.get))

=======
Suggestion 2

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    dict = {}
    for s in S:
        if s in dict:
            dict[s] += 1
        else:
            dict[s] = 1
    print(max(dict, key=dict.get))

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
    s = []
    for i in range(n):
        s.append(input())
    print(max(set(s), key=s.count))

=======
Suggestion 5

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print(max(S, key=S.count))

=======
Suggestion 6

def main():
    N = int(input())
    s = [input() for i in range(N)]
    print(max(set(s), key=s.count))

=======
Suggestion 7

def main():
    # 入力
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())

    # 処理
    S_set = set(S)
    S_dict = {}
    for s in S_set:
        S_dict[s] = 0

    for s in S:
        S_dict[s] += 1

    max_vote = 0
    max_vote_name = ""
    for key, value in S_dict.items():
        if value > max_vote:
            max_vote = value
            max_vote_name = key

    # 出力
    print(max_vote_name)

=======
Suggestion 8

def main():
    n = int(input())
    s = [input() for i in range(n)]
    s_set = set(s)
    ans = ''
    ans_num = 0
    for i in s_set:
        if ans_num < s.count(i):
            ans_num = s.count(i)
            ans = i
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    names = []
    for i in range(n):
        name = input()
        names.append(name)
    print(sorted(names)[n//2])

=======
Suggestion 10

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S = sorted(S)
    #print(S)
    max = 0
    max_name = S[0]
    count = 0
    for i in range(N):
        if S[i] == S[i-1]:
            count += 1
            if count > max:
                max = count
                max_name = S[i]
        else:
            count = 0
    print(max_name)
    return
