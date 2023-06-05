def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(N):
        if a[i] <= i + 1:
            ans = i + 1
    print(ans)

if __name__ == '__main__':
    main()