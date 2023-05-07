def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, N+1):
        min_i = a.index(i)
        max_i = a.index(i, min_i)
        if i == min(a[min_i:max_i+1]):
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()