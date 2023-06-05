def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    for i in range(N-1):
        if H[i] < H[i+1]:
            count = 0
        else:
            count += 1
    print(H[N-1])

if __name__ == '__main__':
    main()