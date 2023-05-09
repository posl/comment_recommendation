def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sumA = [0]
    for i in range(N):
        sumA.append(sumA[i] + A[i])
    #print(sumA)
    results = 0
    for i in range(N+1):
        for j in range(i+1, N+1):
            if sumA[j] - sumA[i] == K:
                results += 1
    print(results)

if __name__ == '__main__':
    main()