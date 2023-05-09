def main():
    #n = int(input())
    n = 44852
    # 1円玉を使う場合
    ans = n
    # 6, 9の累乗を使う場合
    for i in range(1, 100000):
        for j in range(1, 100000):
            if (6**i + 9**j) <= n:
                ans = min(ans, n - (6**i + 9**j))
            else:
                break
    print(ans)

if __name__ == '__main__':
    main()