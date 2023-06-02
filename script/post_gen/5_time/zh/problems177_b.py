Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    min_count = s_len
    for i in range(s_len - t_len + 1):
        count = 0
        for j in range(t_len):
            if s[i + j] != t[j]:
                count += 1
        if count < min_count:
            min_count = count
    print(min_count)

=======
Suggestion 2

def main():
    S = input()
    T = input()
    sLen = len(S)
    tLen = len(T)
    min = 1000
    for i in range(sLen - tLen + 1):
        count = 0
        for j in range(tLen):
            if S[i + j] != T[j]:
                count += 1
        if count < min:
            min = count
    print(min)

=======
Suggestion 3

def main():
    S = input()
    T = input()
    min = 1000
    for i in range(len(S)-len(T)+1):
        count = 0
        for j in range(len(T)):
            if S[i+j] != T[j]:
                count += 1
        if count < min:
            min = count
    print(min)

main()

=======
Suggestion 4

def main():
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)
    s = list(s)
    t = list(t)
    min_change = 1000
    for i in range(len_s - len_t + 1):
        change_cnt = 0
        for j in range(len_t):
            if t[j] != s[i + j]:
                change_cnt += 1
        min_change = min(min_change, change_cnt)
    print(min_change)

=======
Suggestion 5

def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    ans = m
    for i in range(n - m + 1):
        cnt = 0
        for j in range(m):
            if s[i + j] != t[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 6

def count_diff(s1, s2):
    diff_count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff_count += 1
    return diff_count

s = input()
t = input()
min_diff = len(t)
for i in range(len(s) - len(t) + 1):
    diff_count = count_diff(s[i:i+len(t)], t)
    if diff_count < min_diff:
        min_diff = diff_count
print(min_diff)

=======
Suggestion 7

def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    min_change = t_len
    for i in range(s_len - t_len + 1):
        change = 0
        for j in range(t_len):
            if s[i + j] != t[j]:
                change += 1
        if change < min_change:
            min_change = change
    print(min_change)

=======
Suggestion 8

def main():
    s = input()
    t = input()
    print(solve(s, t))

=======
Suggestion 9

def main():
    S = input()
    T = input()
    count = 1000
    for i in range(len(S)-len(T)+1):
        count_tmp = 0
        for j in range(len(T)):
            if S[i+j] != T[j]:
                count_tmp += 1
        if count_tmp < count:
            count = count_tmp
    print(count)

=======
Suggestion 10

def main():
    s = input()
    t = input()
    minChange = 1000
    for i in range(len(s)-len(t)+1):
        change = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                change += 1
        if minChange > change:
            minChange = change
    print(minChange)
