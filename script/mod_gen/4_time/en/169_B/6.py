def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    if 0 in a:
        print(0)
        return
    ans = 1
    for i in a:
        ans *= i
        if ans > 10**18:
            print(-1)
            return
    print(ans)

if __name__ == '__main__':
    main()