def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    ans = 1
    n = 7 % K
    while n != 0:
        n = (n * 10 + 7) % K
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()