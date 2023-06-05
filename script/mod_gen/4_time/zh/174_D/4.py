def main():
    n = int(input())
    colors = list(input())
    left = 0
    right = n - 1
    count = 0
    while left < right:
        if colors[left] == 'W':
            while left < right and colors[right] == 'W':
                right -= 1
            if left < right:
                colors[left], colors[right] = colors[right], colors[left]
                count += 1
                left += 1
                right -= 1
        else:
            left += 1
    print(count)

if __name__ == '__main__':
    main()