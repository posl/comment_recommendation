Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()
    S_len = len(S)
    T_len = len(T)
    for x in range(T_len+1):
        S_ = S[:x] + S[S_len-(T_len-x):]
        if S_ == T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 2

def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    for i in range(0,t_len+1):
        flag = True
        for j in range(0,i):
            if s[j] != '?' and s[j] != t[j]:
                flag = False
        for j in range(i,s_len-t_len+i):
            if s[j] != '?':
                flag = False
        for j in range(i,t_len):
            if s[s_len-t_len+i+j] != '?' and s[s_len-t_len+i+j] != t[j]:
                flag = False
        if flag:
            print('Yes')
        else:
            print('No')

=======
Suggestion 3

def problem287_d():
    pass

=======
Suggestion 4

def main():
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)
    for i in range(len_t+1):
        s1 = s[:i] + t[i:] #前i个字符和后len_t-i个字符
        s2 = s[len_s-len_t+i:] + s[:len_s-len_t+i] #后len_t-i个字符和前len_s-len_t+i个字符
        s3 = s[len_s-len_t+i:] + t[:len_t-i] #后len_t-i个字符和前len_t-i个字符
        if s1.replace('?', 'a') == t:
            print('Yes')
        elif s2.replace('?', 'a') == t:
            print('Yes')
        elif s3.replace('?', 'a') == t:
            print('Yes')
        else:
            print('No')
main()

=======
Suggestion 5

def main():
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)
    for x in range(len_t + 1):
        s_new = s[:len_t - x] + s[len_s - x:]
        flag = True
        for i in range(len_t):
            if s_new[i] != t[i] and s_new[i] != '?':
                flag = False
                break
        if flag:
            print("Yes")
        else:
            print("No")

=======
Suggestion 6

def main():
    # 读取输入
    s = input()
    t = input()

    # 计算匹配数
    count = 0
    for i in range(len(t)):
        if t[i] == '?':
            count += 1

    # 计算匹配结果
    for i in range(len(s) - len(t) + 1):
        flag = True
        for j in range(len(t)):
            if s[i + j] != t[j] and s[i + j] != '?':
                flag = False
                break
        if flag:
            print('Yes')
        else:
            print('No')

=======
Suggestion 7

def main():
    s = input()
    t = input()
    for i in range(len(s)-len(t)+1):
        if t == s[:i] + t + s[i+len(t):]:
            print("Yes")
        else:
            print("No")

=======
Suggestion 8

def main():
    s = input()
    t = input()
    tlen = len(t)
    slen = len(s)
    s1 = s.replace('?','a')
    s2 = s.replace('?','z')
    if tlen == slen:
        if t == s1:
            print('Yes')
        else:
            print('No')
    else:
        for i in range(slen-tlen+1):
            if t == s1[i:i+tlen] or t == s2[i:i+tlen]:
                print('Yes')
            else:
                print('No')

=======
Suggestion 9

def main():
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)
    if len_s < len_t:
        print("No\n" * (len_t + 1))
        return
    s = list(s)
    t = list(t)
    for i in range(len_s - len_t + 1):
        for j in range(len_t):
            if s[i + j] != t[j] and s[i + j] != "?":
                break
        else:
            print("Yes\n" * (i + 1) + "No\n" * (len_t - i) + "Yes\n" * (len_s - len_t - i))
            return
    print("No\n" * (len_t + 1))

=======
Suggestion 10

def problems287_d():
    pass
