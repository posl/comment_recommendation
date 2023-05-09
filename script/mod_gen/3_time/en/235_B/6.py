def main():
    N = int(input())
    H = [int(x) for x in input().split()]
    maxH = 0
    for i in range(N):
        if H[i] >= maxH:
            maxH = H[i]
    print(maxH)

if __name__ == '__main__':
    main()