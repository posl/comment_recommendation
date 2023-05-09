def takoyaki():
    N = int(input())
    D = list(map(int, input().split()))
    sum = 0
    for i in range(N-1):
        for j in range(i+1, N):
            sum += D[i] * D[j]
    return sum

if __name__ == '__main__':
    takoyaki()