def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.insert(0, 0)
    count = 0
    for i in range(1, n+1):
        if h[i] < h[i-1]:
            count += h[i-1] - h[i]
    print(count)

if __name__ == '__main__':
    main()