def main():
    N = int(input())
    H = list(map(int, input().split()))
    #print(N)
    #print(H)
    maxH = 0
    for i in range(N):
        if H[i] >= maxH:
            maxH = H[i]
    print(maxH)

if __name__ == '__main__':
    main()