def main():
    n, x = map(int, input().split())
    ans = chr(ord('A') + (x - 1) // n)
    print(ans)

if __name__ == '__main__':
    main()