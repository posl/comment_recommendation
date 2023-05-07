def main():
    N = int(input())
    H = list(map(int, input().split()))
    maxH = H[0]
    cnt = 1
    for i in range(1, N):
        if maxH <= H[i]:
            cnt += 1
            maxH = H[i]
    print(cnt)

if __name__ == '__main__':
    main()