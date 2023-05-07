def main():
    # Get input
    n = int(input())
    a = list(map(int, input().split()))
    # Calculate
    sum = 0
    for i in range(1, n):
        for j in range(i):
            sum += (a[i] - a[j]) ** 2
    # Output
    print(sum)

if __name__ == '__main__':
    main()