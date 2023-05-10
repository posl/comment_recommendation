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
