def main():
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0)
    else:
        ans = 1
        for i in a:
            ans *= i
            if ans > 10 ** 18:
                print(-1)
                exit()
        print(ans)

if __name__ == '__main__':
    main()