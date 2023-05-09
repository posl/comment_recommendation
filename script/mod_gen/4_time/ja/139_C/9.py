def main():
    n = int(input())
    heights = [int(i) for i in input().split()]
    max_count = 0
    count = 0
    for i in range(1, n):
        if heights[i-1] >= heights[i]:
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    print(max_count)

if __name__ == '__main__':
    main()