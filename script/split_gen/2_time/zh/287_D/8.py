def main():
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)
    if len_s < len_t:
        print('No')
        return
    for i in range(len_s - len_t + 1):
        if s[i] == t[0] or s[i] == '?':
            for j in range(1, len_t):
                if s[i + j] != t[j] and s[i + j] != '?':
                    break
            else:
                print('Yes')
                return
    print('No')
