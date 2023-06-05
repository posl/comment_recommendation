def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(1 << n):
        sum = 0
        cnt = 0
        for j in range(n):
            if i & 1 << j:
                sum += a[j]
                cnt += 1
        if sum % cnt == 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()