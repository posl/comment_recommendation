def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    if 0 in a_list:
        print(0)
        return
    ans = 1
    for a in a_list:
        ans *= a
        if ans > 1000000000000000000:
            print(-1)
            return
    print(ans)

if __name__ == '__main__':
    main()