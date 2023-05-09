def main():
    # Get input
    N = int(input()) # Number of Takoyaki
    d = list(map(int, input().split())) # Deliciousness of Takoyaki
    # Compute the sum of the health points restored from eating two takoyaki over all possible choices of two takoyaki from the N takoyaki served.
    sum = 0
    for i in range(N-1):
        for j in range(i+1, N):
            sum += d[i] * d[j]
    # Print the sum of the health points restored from eating two takoyaki over all possible choices of two takoyaki from the N takoyaki served.
    print(sum)

if __name__ == '__main__':
    main()