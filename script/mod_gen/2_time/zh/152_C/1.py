def main():
    n = int(input())
    p = list(map(int, input().split()))
    min_p = p[0]
    count = 1
    for i in range(1, n):
        if min_p >= p[i]:
            count += 1
        min_p = min(min_p, p[i])
    print(count)

if __name__ == '__main__':
    main()