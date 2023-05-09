def main():
    X = int(input())
    ans = X // 500 * 1000
    ans += X % 500 // 5 * 5
    print(ans)

if __name__ == '__main__':
    main()