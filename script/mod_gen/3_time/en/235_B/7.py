def main():
    N = int(input())
    H = list(map(int, input().split()))
    maxH = 0
    count = 0
    for h in H:
        if h >= maxH:
            count += 1
            maxH = h
    print(maxH)

if __name__ == '__main__':
    main()