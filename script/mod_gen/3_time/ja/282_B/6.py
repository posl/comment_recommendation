def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if 'o' in s[i] + s[j]:
                count += 1
    print(count)

if __name__ == '__main__':
    main()