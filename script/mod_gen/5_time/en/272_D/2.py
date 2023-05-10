def main():
    n, m = map(int, input().split())
    if n == 1:
        print(0)
        return
    if m == 1:
        for i in range(n):
            print(i)
        return
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                print(0, end=' ')
                continue
            if i == 1 and j == 0:
                print(1, end=' ')
                continue
            if i == 0 and j == 1:
                print(1, end=' ')
                continue
            if i == 1 and j == 1:
                print(2, end=' ')
                continue
            if i == 0 or j == 0 or i == 1 or j == 1:
                print(2, end=' ')
                continue
            print(3, end=' ')
        print()

if __name__ == '__main__':
    main()