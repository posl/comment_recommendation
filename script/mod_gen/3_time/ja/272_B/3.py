def main():
    N, M = map(int, input().split())
    d = {}
    for i in range(M):
        k, *x = map(int, input().split())
        for j in x:
            if j in d:
                d[j] += 1
            else:
                d[j] = 1
    print('Yes' if all(i == M for i in d.values()) else 'No')

if __name__ == '__main__':
    main()