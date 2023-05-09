def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    max_count = 0
    for i in range(1, n):
        if h[i-1] >= h[i]:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    print(max_count)

if __name__ == '__main__':
    main()