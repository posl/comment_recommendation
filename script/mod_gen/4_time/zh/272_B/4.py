def main():
    n, m = map(int, input().split())
    a = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        a[i] = list(map(int, input().split()))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(m):
                if i+1 in a[k] and j+1 in a[k]:
                    break
            else:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()