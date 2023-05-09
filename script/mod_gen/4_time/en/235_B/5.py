def main():
    n = int(input())
    h = list(map(int, input().split()))
    max = 0
    count = 0
    for i in range(1, n):
        if h[i-1] >= h[i]:
            count += 1
        else:
            count = 0
        if max < count:
            max = count
    print(max)

if __name__ == '__main__':
    main()