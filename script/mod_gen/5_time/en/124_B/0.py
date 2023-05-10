def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 1
    max = H[0]
    for i in range(1, N):
        if max <= H[i]:
            count += 1
            max = H[i]
    print(count)

if __name__ == '__main__':
    main()