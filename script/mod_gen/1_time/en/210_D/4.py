def main():
    H, W, C = list(map(int, input().split()))
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    min_cost = 10**18
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if i == k and j == l:
                        continue
                    cost = A[i][j] + A[k][l] + C*abs(i-k) + C*abs(j-l)
                    if cost < min_cost:
                        min_cost = cost
    print(min_cost)

if __name__ == '__main__':
    main()