def main():
    N = int(input())
    A = list(map(int, input().split()))
    if 0 in A:
        print(0)
        return
    ans = 1
    for i in A:
        ans *= i
        if ans > 10**18:
            print(-1)
            return
    print(ans)

if __name__ == '__main__':
    main()