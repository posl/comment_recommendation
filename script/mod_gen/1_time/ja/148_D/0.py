def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if a[i] != i+1:
            ans += 1
    if ans > 2:
        print(-1)
    else:
        print(ans)
main()

if __name__ == '__main__':
    main()