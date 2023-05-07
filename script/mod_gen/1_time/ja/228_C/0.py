def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort(key=lambda x: x[0] + x[1] + x[2], reverse=True)
    score = sum(P[K - 1])
    count = 0
    for i in range(N):
        if score < sum(P[i]):
            count += 1
    if count < K:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()