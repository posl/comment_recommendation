def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    highest = h[0]
    for i in range(1, n):
        if h[i] >= highest:
            count += 1
        highest = max(highest, h[i])
    print(count + 1)

if __name__ == '__main__':
    main()