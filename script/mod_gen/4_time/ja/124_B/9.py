def main():
    N = int(input())
    H = list(map(int, input().split()))
    max = 0
    count = 0
    for i in range(0, N):
        if max <= H[i]:
            count += 1
            max = H[i]
    print(count)

if __name__ == '__main__':
    main()