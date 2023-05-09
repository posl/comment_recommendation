def main():
    N, X = map(int, input().split())
    ans = ""
    for i in range(1, N + 1):
        ans += chr(65 + (X - i) // N)
    print(ans)
main()

if __name__ == '__main__':
    main()