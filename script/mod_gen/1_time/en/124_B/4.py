def main():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 0
    max = 0
    for i in range(N):
        if H[i] >= max:
            cnt += 1
            max = H[i]
    print(cnt)

if __name__ == '__main__':
    main()