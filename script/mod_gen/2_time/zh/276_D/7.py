def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        flag = True
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] = a[i] // 2
            else:
                flag = False
                break
        if flag:
            ans += 1
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()