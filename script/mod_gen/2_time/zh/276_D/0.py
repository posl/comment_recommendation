def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        if all([a[i] % 2 == 0 for i in range(N)]):
            a = [a[i] // 2 for i in range(N)]
            ans += 1
        else:
            break
    print(ans)
    return

if __name__ == '__main__':
    main()