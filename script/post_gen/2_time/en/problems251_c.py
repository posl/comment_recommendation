Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    score = {}
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if s not in score:
            score[s] = t
    print(n - len(score) + 1)

=======
Suggestion 2

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    max_score = 0
    max_score_index = 0
    for i in range(N):
        if S[i] not in S[:i] and T[i] > max_score:
            max_score = T[i]
            max_score_index = i
    print(max_score_index+1)

=======
Suggestion 3

def solve():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    d = {}
    for i in range(N-1, -1, -1):
        if S[i] not in d:
            d[S[i]] = T[i]
    print(N - len(d))

=======
Suggestion 4

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S_i, T_i = input().split()
        S.append(S_i)
        T.append(int(T_i))

    #print(S)
    #print(T)

    # 既出の文字列を記録
    S_set = set()
    # 各文字列の最高得点を記録
    T_max = {}
    # 各文字列の最高得点を記録したSubmissionのインデックスを記録
    T_max_index = {}
    for i in range(N):
        if S[i] not in S_set:
            S_set.add(S[i])
            T_max[S[i]] = T[i]
            T_max_index[S[i]] = i
        else:
            if T[i] > T_max[S[i]]:
                T_max[S[i]] = T[i]
                T_max_index[S[i]] = i

    #print(S_set)
    #print(T_max)
    #print(T_max_index)

    # 各文字列の最高得点を記録したSubmissionのインデックスのうち、最小のものを探す
    T_max_index_min = N
    for s in S_set:
        T_max_index_min = min(T_max_index_min, T_max_index[s])

    print(T_max_index_min + 1)

=======
Suggestion 5

def main():
    N = int(input())
    submissions = []
    for i in range(N):
        S, T = input().split()
        submissions.append([S, int(T), i + 1])
    submissions = sorted(submissions, key=lambda x: x[2])
    submissions = sorted(submissions, key=lambda x: x[1], reverse=True)
    best = []
    for i in range(N):
        if submissions[i][0] not in [s[0] for s in best]:
            best.append(submissions[i])
    print(best[0][2])

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        a, b = input().split()
        s.append(a)
        t.append(int(b))
    best = 0
    best_index = 0
    for i in range(n):
        if s[i] not in s[:i] and best < t[i]:
            best = t[i]
            best_index = i
    print(best_index + 1)

=======
Suggestion 7

def main():
    n = int(input())
    dict = {}
    for i in range(n):
        s, t = input().split()
        if s in dict:
            dict[s].append([i, int(t)])
        else:
            dict[s] = [[i, int(t)]]
    max = 0
    max_index = 0
    for key, value in dict.items():
        if len(value) == 1:
            if value[0][1] > max:
                max = value[0][1]
                max_index = value[0][0]
        else:
            value.sort(key=lambda x: x[1], reverse=True)
            if value[0][1] > max:
                max = value[0][1]
                max_index = value[0][0]
    print(max_index + 1)

=======
Suggestion 8

def main():
    N = int(input())
    S = []
    T = []
    for _ in range(N):
        st = input().split()
        S.append(st[0])
        T.append(int(st[1]))
    T_max = max(T)
    T_max_idx = T.index(T_max)
    S_max = S[T_max_idx]
    T_max_idx2 = 0
    for i in range(N):
        if T[i] == T_max and S[i] == S_max:
            T_max_idx2 = i
            break
    print(T_max_idx2 + 1)

=======
Suggestion 9

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))

    # 1. 元の提出を抽出する
    # 2. 最高得点の提出を抽出する
    # 3. 最高得点の提出のうち、最も早い提出を抽出する
    # 4. 3の提出の番号を出力する

    # 1. 元の提出を抽出する
    original_submissions = []
    for i in range(N):
        # S[i] が S[:i] に存在するかどうか
        if S[i] not in S[:i]:
            original_submissions.append(i)

    # 2. 最高得点の提出を抽出する
    best_submissions = []
    best_score = -1
    for i in original_submissions:
        if T[i] > best_score:
            best_score = T[i]

    # 3. 最高得点の提出のうち、最も早い提出を抽出する
    best_submission = -1
    for i in original_submissions:
        if T[i] == best_score:
            best_submission = i
            break

    # 4. 3の提出の番号を出力する
    print(best_submission + 1)
