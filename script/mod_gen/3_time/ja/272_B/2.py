def main():
    n, m = map(int, input().split())
    x = [list(map(int, input().split()))[1:] for _ in range(m)]
    for i in range(m):
        x[i].sort()
    for i in range(m):
        for j in range(i+1, m):
            if x[i] == x[j]:
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    main()