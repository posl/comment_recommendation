def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    count = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            count += 1
        else:
            count = 0
        ans = max(ans, count)
    print(ans)

if __name__ == '__main__':
    main()