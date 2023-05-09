def main():
    N = int(input())
    H = list(map(int, input().split()))
    max_height = H[0]
    for i in range(1, N):
        if max_height <= H[i]:
            max_height = H[i]
    print(max_height)

if __name__ == '__main__':
    main()