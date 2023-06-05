def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    for i in range(n-m+1):
        for j in range(m):
            if s[i+j] != t[j] and s[i+j] != '?':
                break
        else:
            print('Yes')
            break
    else:
        print('No')
