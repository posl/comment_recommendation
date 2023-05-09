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
            print(''.join(s[:i] + t + s[i+m:]).replace('?', 'a'))
            break
    else:
        print('UNRESTORABLE')

if __name__ == '__main__':
    main()