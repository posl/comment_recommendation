def main():
    N = int(input())
    H = list(map(int, input().split()))
    max_h = H[0]
    count = 0
    for i in range(1, N):
        if max_h <= H[i]:
            count += 1
            max_h = H[i]
    print(count)

if __name__ == '__main__':
    main()