def main():
    n = int(input())
    h = [int(i) for i in input().split()]
    count = 1
    max_count = 1
    for i in range(1, n):
        if h[i-1] >= h[i]:
            count += 1
        else:
            if max_count < count:
                max_count = count
            count = 1
    if max_count < count:
        max_count = count
    print(max_count-1)

if __name__ == '__main__':
    main()