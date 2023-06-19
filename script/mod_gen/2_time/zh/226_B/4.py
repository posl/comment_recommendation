def main():
    N = int(input())
    d = {}
    for i in range(N):
        L = int(input().split()[0])
        s = input().split()
        if L == 1:
            if s[0] in d.keys():
                d[s[0]] += 1
            else:
                d[s[0]] = 1
        else:
            if s[0] in d.keys():
                d[s[0]] += 1
            else:
                d[s[0]] = 1
            if s[-1] in d.keys():
                d[s[-1]] += 1
            else:
                d[s[-1]] = 1
    print(len(d.keys()))

if __name__ == '__main__':
    main()