def main():
    N = int(input())
    H = list(map(int, input().split()))
    max = H[0]
    for i in range(1, N):
        if H[i] >= max:
            max = H[i]
    print(max)

if __name__ == '__main__':
    main()