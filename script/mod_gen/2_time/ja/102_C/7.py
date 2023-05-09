def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 10**9
    for i in range(n):
        tmp = a[i] - (i+1)
        ans = min(ans, tmp)
    ans = abs(ans)
    sum = 0
    for i in range(n):
        sum += abs(a[i] - (i+1) - ans)
    print(sum)

if __name__ == '__main__':
    main()