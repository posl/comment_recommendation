def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    weight = [0] * N
    for i in range(N):
        if A[i] <= W:
            weight[i] = 1
    #print(weight)
    total = 0
    for i in range(N):
        if weight[i] == 1:
            total += 1
    #print(total)
    for i in range(N-1):
        for j in range(i+1, N):
            if weight[i] == 1 and weight[j] == 1 and A[i] + A[j] <= W:
                total += 1
    #print(total)
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if weight[i] == 1 and weight[j] == 1 and weight[k] == 1 and A[i] + A[j] + A[k] <= W:
                    total += 1
    print(total)

if __name__ == '__main__':
    main()