def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    if 0 in a_list:
        print(0)
        return
    ans = 1
    for i in range(n):
        ans *= a_list[i]
        if ans > 10**18:
            print(-1)
            return
    print(ans)

if __name__ == '__main__':
    main()