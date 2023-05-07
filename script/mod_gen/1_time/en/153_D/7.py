def main():
    H = int(input())
    ans = 0
    while H > 0:
        H //= 2
        ans = ans * 2 + 1
    print(ans)

if __name__ == '__main__':
    main()