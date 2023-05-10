def main():
    H,W,C = map(int, input().split())
    A = [[0 for i in range(W)] for j in range(H)]
    for i in range(H):
        A[i] = list(map(int, input().split()))
    min_cost = 10**18
    for i in range(H):
        for j in range(W):
            for k in range(i, H):
                for l in range(j, W):
                    if i == k and j == l:
                        continue
                    cost = A[i][j] + A[k][l] + C*(abs(i-k) + abs(j-l))
                    if cost < min_cost:
                        min_cost = cost
    print(min_cost)

if __name__ == '__main__':
    main()