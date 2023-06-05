def main():
    n = int(input())
    a = list(map(int, input().split()))
    # print(a)
    # print(n)
    # a = [2, 1, 5, 4, 3]
    # n = 5
    ans = 0
    for i in range(n):
        if a[i] > ans:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()