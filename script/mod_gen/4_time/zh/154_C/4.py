def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    flag = 0
    for i in range(n-1):
        if a[i] == a[i+1]:
            flag = 1
            break
    if flag == 1:
        print('NO')
    else:
        print('YES')

if __name__ == '__main__':
    main()