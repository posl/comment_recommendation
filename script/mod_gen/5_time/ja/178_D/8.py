def main():
    s = int(input())
    ans = 0
    for i in range(1, s//3 + 1):
        ans += (s - 3*i) // 2
    print(ans%1000000007)

if __name__ == '__main__':
    main()