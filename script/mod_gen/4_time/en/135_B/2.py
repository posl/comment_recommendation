def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n):
        if p[i-1] != i:
            count += 1
    if count <= 2:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()