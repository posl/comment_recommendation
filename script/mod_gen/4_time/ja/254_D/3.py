def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            if i*j <= n and i == j:
                ans += 1
            elif i*j <= n and i != j:
                ans += 2
    print(ans)

if __name__ == '__main__':
    main()