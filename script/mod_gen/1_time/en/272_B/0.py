def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split()))[1:] for _ in range(m)]
    for i in range(n):
        for j in range(i + 1, n):
            if not any(i + 1 in x and j + 1 in x for x in a):
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()