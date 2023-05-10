def main():
    n = int(input())
    heights = list(map(int, input().split()))
    max_height = 0
    for i in range(n-1):
        if heights[i] < heights[i+1]:
            max_height = heights[i+1]
    print(max_height)

if __name__ == '__main__':
    main()