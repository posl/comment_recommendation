def main():
    N, K = map(int, input().split())
    #print(N, K)
    sum = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            sum += i*100 + j
    print(sum)
