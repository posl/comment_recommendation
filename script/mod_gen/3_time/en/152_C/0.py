def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    min_p = n + 1
    for i in range(n):
        if p[i] <= min_p:
            count += 1
            min_p = p[i]
    print(count)

if __name__ == '__main__':
    main()