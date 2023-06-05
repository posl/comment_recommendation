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
