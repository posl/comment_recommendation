def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(1, n):
        if p[i-1] > p[i]:
            cnt += 1
    if cnt <= 2:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()