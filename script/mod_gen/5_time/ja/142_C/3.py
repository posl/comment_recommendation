def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0]*n
    for i in range(n):
        ans[a[i]-1] = i+1
    print(*ans)

if __name__ == '__main__':
    main()