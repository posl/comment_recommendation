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
