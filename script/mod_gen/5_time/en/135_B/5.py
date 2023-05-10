def main():
    N = int(input())
    p = list(map(int, input().split()))
    p_sorted = sorted(p)
    if p == p_sorted:
        print('YES')
    else:
        for i in range(N):
            for j in range(i+1, N):
                p[i], p[j] = p[j], p[i]
                if p == p_sorted:
                    print('YES')
                    return
                p[i], p[j] = p[j], p[i]
        print('NO')

if __name__ == '__main__':
    main()