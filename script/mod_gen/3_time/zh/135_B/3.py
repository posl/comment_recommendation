def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n-1):
        if p[i] > p[i+1]:
            count += 1
    if count <= 1:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()