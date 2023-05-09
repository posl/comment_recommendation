def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    cnt = 0
    for i in range(1, n - 1):
        if p[i] > p[i - 1] and p[i] < p[i + 1]:
            cnt += 1
        elif p[i] < p[i - 1] and p[i] > p[i + 1]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()