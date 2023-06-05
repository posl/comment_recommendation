def main():
    s = input()
    t = input()
    n = len(t)
    m = len(s)
    for i in range(m-n+1):
        flag = True
        for j in range(n):
            if s[i+j] != t[j] and s[i+j] != '?':
                flag = False
                break
        if flag:
            print('Yes')
        else:
            print('No')
    for i in range(m-n+1,m):
        print('No')
