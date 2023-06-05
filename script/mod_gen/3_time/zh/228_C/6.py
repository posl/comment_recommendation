def main():
    n, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    a.sort(key=lambda x: sum(x), reverse=True)
    a = a[:k]
    for i in range(n):
        for j in range(3):
            if a[0][j] < a[i][j]:
                print('No')
                break
        else:
            print('Yes')

if __name__ == '__main__':
    main()