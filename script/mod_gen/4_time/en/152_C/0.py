def main():
    N = int(input())
    P = list(map(int, input().split()))
    cnt = 0
    minP = P[0]
    for i in range(N):
        if P[i] <= minP:
            cnt += 1
        minP = min(minP, P[i])
    print(cnt)

if __name__ == '__main__':
    main()