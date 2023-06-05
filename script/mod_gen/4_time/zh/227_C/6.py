def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        for j in range(i, n+1, i):
            for k in range(j, n+1, j):
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()