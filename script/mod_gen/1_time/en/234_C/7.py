def main():
    K = int(input())
    ans = 0
    for i in range(1, 100):
        ans += 2 ** i
    ans += K - 1
    print(ans)

if __name__ == '__main__':
    main()