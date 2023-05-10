def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1
    if 0 in A:
        ans = 0
    else:
        for a in A:
            ans *= a
            if ans > 10**18:
                ans = -1
                break
    print(ans)

if __name__ == '__main__':
    main()