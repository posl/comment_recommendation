def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    max = 0
    for i in range(N - 1):
        if H[i] >= H[i + 1]:
            count += 1
        else:
            count = 0
        if max < count:
            max = count
    print(max)

if __name__ == '__main__':
    main()