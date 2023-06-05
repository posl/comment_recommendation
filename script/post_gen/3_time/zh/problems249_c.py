Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1 << N):
        if bin(i).count("1") != K:
            continue
        cnt = 0
        for j in range(N):
            if i >> j & 1:
                cnt |= set(S[j])
        ans = max(ans, bin(cnt).count("1"))
    print(ans)

=======
Suggestion 2

def get_max_num_of_alphabets(N, K, S):
    max_num = 0
    for i in range(2**N):
        tmp = i
        tmp_num = 0
        alphabets = []
        while tmp > 0:
            if tmp % 2 == 1:
                alphabets.append(S[tmp_num])
            tmp_num += 1
            tmp = tmp >> 1
        if len(set(alphabets)) == K:
            max_num = max(max_num, len(set(alphabets)))
    return max_num

=======
Suggestion 3

def get_k_str(k, str_list):
    str_list = sorted(str_list, key=lambda x: len(x))
    str_list = str_list[:k]
    str_list = sorted(str_list, key=lambda x: len(set(x)))
    return str_list

=======
Suggestion 4

def check(s1, s2):
    for i in s1:
        if i in s2:
            return True
    return False

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    S = []
    for i in range(N):
        S.append(input())
    ans = 0
    for i in range(1 << N):
        tmp = []
        for j in range(N):
            if (i >> j) & 1:
                tmp.append(S[j])
        if len(tmp) != K:
            continue
        cnt = 0
        for j in range(26):
            flag = True
            for k in range(K):
                if chr(j + 97) not in tmp[k]:
                    flag = False
            if flag:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())
    ans = 0
    for i in range(1 << n):
        cnt = 0
        for j in range(n):
            if i >> j & 1:
                cnt += 1
        if cnt != k:
            continue
        tmp = set()
        for j in range(n):
            if i >> j & 1:
                for c in s[j]:
                    tmp.add(c)
        if len(tmp) == k:
            ans = max(ans, cnt)
    print(ans)

=======
Suggestion 7

def get_input():
    n,k = input().split()
    n = int(n)
    k = int(k)
    s = []
    for i in range(n):
        s.append(input())
    return n,k,s

=======
Suggestion 8

def dfs(i, cnt, used, n, k, s):
    if i == n:
        return cnt == k
    if dfs(i + 1, cnt, used, n, k, s):
        return True
    for j in range(len(s[i])):
        if not used[ord(s[i][j]) - ord('a')]:
            used[ord(s[i][j]) - ord('a')] = True
            cnt += 1
    if dfs(i + 1, cnt, used, n, k, s):
        return True
    for j in range(len(s[i])):
        if not used[ord(s[i][j]) - ord('a')]:
            used[ord(s[i][j]) - ord('a')] = False
            cnt -= 1
    return False

=======
Suggestion 9

def get_alpha_num(s):
    alpha_num = 0
    for i in range(26):
        if chr(ord('a') + i) in s:
            alpha_num += 1
    return alpha_num

=======
Suggestion 10

def get_all_subsets(ss):
    return get_all_subsets_recur([], sorted(ss))
