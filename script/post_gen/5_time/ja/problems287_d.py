Synthesizing 10/10 solutions

=======
Suggestion 1

def input_data():
    S = input()
    T = input()
    return S, T

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if len(s) < len(t):
        print('No')
        exit()
    for i in range(len(s) - len(t) + 1):
        flag = True
        for j in range(len(t)):
            if s[i + j] != '?' and s[i + j] != t[j]:
                flag = False
                break
        if flag:
            print('Yes')
        else:
            print('No')

=======
Suggestion 3

def main():
    S = input()
    T = input()
    s_len = len(S)
    t_len = len(T)

    for i in range(t_len):
        if S[s_len - t_len + i] != T[i] and S[s_len - t_len + i] != '?':
            print('No')
            return

    print('Yes')

main()

=======
Suggestion 4

def main():
    s = input()
    t = input()
    t_len = len(t)
    s_len = len(s)
    for x in range(0, t_len + 1):
        if s[0:x] + s[s_len - t_len + x:s_len] == t:
            print('Yes')
        else:
            print('No')

=======
Suggestion 5

def check(s, t, x):
    for i in range(x):
        if s[i] != '?' and s[i] != t[i]:
            return False
    for i in range(len(t)):
        if s[i+x] != '?' and s[i+x] != t[i]:
            return False
    return True

=======
Suggestion 6

def match(s,t):
    for i in range(len(t)):
        if s[i] == '?':
            continue
        if s[i] != t[i]:
            return False
    return True

s = input()
t = input()
n = len(s)
m = len(t)

for i in range(n-m+1):
    if match(s[i:i+m],t):
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def check(s, t):
    for i in range(len(t)):
        if s[i] != '?' and s[i] != t[i]:
            return False
    return True

s = input()
t = input()
for i in range(len(s) - len(t) + 1):
    if check(s[i:i+len(t)], t):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    for i in range(n - m + 1):
        if all(s[i + j] == t[j] or s[i + j] == '?' for j in range(m)):
            print('Yes')
        else:
            print('No')

=======
Suggestion 9

def solve():
    s = input()
    t = input()

    # tの?をaに置き換えた文字列を作成
    t_list = list(t)
    for i in range(len(t)):
        if t_list[i] == '?':
            t_list[i] = 'a'
    t_a = ''.join(t_list)

    # sの先頭からtの長さ分の文字列を作成
    s_a = s[:len(t)]

    # tの?をaに置き換えた文字列とsの先頭からtの長さ分の文字列が一致したらYes
    if s_a == t_a:
        print('Yes')
    else:
        print('No')

    # sの先頭からtの長さ分の文字列を作成
    s_b = s[-len(t):]

    # tの?をaに置き換えた文字列とsの末尾からtの長さ分の文字列が一致したらYes
    if s_b == t_a:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    s = input()
    t = input()
    ls = len(s)
    lt = len(t)
    for i in range(ls - lt + 1):
        s1 = s[:i]
        s2 = s[i + lt:]
        s3 = s1 + t + s2
        flag = True
        for j in range(ls):
            if s3[j] != s[j] and s3[j] != '?':
                flag = False
                break
        if flag:
            print('Yes')
        else:
            print('No')
