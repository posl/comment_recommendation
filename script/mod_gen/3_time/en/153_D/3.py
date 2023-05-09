def main():
    H = int(input())
    ans = 1
    while H > 1:
        ans += H
        H //= 2
    print(ans)

if __name__ == '__main__':
    main()