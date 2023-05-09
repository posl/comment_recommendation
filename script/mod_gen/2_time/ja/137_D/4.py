def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    B = [0] * (M + 1)
    for i in range(M):
        B[i + 1] = B[i]
        while AB and AB[0][0] == i + 1:
            B[i + 1] = max(B[i + 1], AB[0][1])
            AB.pop(0)
        if i > 0:
            B[i + 1] = max(B[i + 1], B[i])
    print(B[-1])

if __name__ == '__main__':
    main()