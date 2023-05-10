def main():
    N = int(input())
    H = list(map(int, input().split()))
    max = H[0]
    for i in range(1, N):
        if max < H[i]:
            max = H[i]
    print(H.index(max) + 1)

if __name__ == '__main__':
    main()