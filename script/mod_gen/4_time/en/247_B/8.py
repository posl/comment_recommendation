def main():
    n = int(input())
    st = [input().split() for _ in range(n)]
    st_s = [s for s, t in st]
    st_t = [t for s, t in st]
    for i in range(n):
        if st_s[i] in st_t[:i]:
            print('Yes')
            return
        if st_t[i] in st_s[:i]:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()