def main():
    K = int(input())
    ans = 0
    for i in range(1, K + 1):
        if i % 2 == 0:
            ans += K // 2
        else:
            ans += (K + 1) // 2
    print(ans)

if __name__ == '__main__':
    main()