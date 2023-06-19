def main():
    n = int(input())
    h = list(map(int, input().split()))
    maxH = 0
    for i in range(n):
        if h[i] >= maxH:
            maxH = h[i]
    print(maxH)

if __name__ == '__main__':
    main()