def main():
    N, M = map(int, input().split())
    p = [0 for _ in range(N)]
    s = [0 for _ in range(N)]
    for _ in range(M):
        i, j = map(str, input().split())
        i = int(i)
        if s[i-1] == 0:
            if j == 'AC':
                p[i-1] += 1
                s[i-1] = 1
            else:
                p[i-1] += 0
                s[i-1] = 0
        else:
            p[i-1] += 0
            s[i-1] = 1
    print(sum(s), sum(p))

if __name__ == '__main__':
    main()