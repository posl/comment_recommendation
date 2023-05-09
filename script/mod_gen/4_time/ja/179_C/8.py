def main():
    n = int(input())
    ans = 0
    for i in range(1,n):
        for j in range(1,n):
            if i * j + 1 > n:
                break
            elif i * j + 1 == n:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()