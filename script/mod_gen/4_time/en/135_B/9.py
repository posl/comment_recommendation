def main():
    N = int(input())
    p = list(map(int, input().split()))
    q = list(range(1, N+1))
    if p == q:
        print('YES')
    else:
        for i in range(N):
            for j in range(i+1, N):
                r = p[:]
                r[i], r[j] = r[j], r[i]
                if r == q:
                    print('YES')
                    return
        print('NO')

if __name__ == '__main__':
    main()