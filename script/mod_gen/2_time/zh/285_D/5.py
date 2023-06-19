def main():
    n = int(input())
    s_t = [input().split() for _ in range(n)]
    s = [s_t[i][0] for i in range(n)]
    t = [s_t[i][1] for i in range(n)]
    for i in range(n):
        if s[i] in t:
            t.remove(s[i])
    if len(t) == 1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()