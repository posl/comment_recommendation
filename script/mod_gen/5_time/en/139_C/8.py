def main():
    n = int(input())
    heights = list(map(int, input().split()))
    max_count = 0
    count = 0
    for i in range(0, n-1):
        if heights[i] >= heights[i+1]:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    print(max_count)

if __name__ == '__main__':
    main()