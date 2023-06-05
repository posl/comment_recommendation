def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n+1):
        for j in range(n-i+1):
            avg = sum(a[j:j+i]) / i
            if avg == int(avg):
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()