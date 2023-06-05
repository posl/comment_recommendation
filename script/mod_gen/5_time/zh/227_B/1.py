def main():
    n = int(input())
    s = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(1, 1001):
            if (j * (j + 1) * 4 + 3 * (j + 1) + 3 * j) == s[i]:
                break
            elif (j * (j + 1) * 4 + 3 * (j + 1) + 3 * j) > s[i]:
                count += 1
                break
    print(count)

if __name__ == '__main__':
    main()