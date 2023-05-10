def main():
    N = int(input())
    X = list(map(int, input().split()))
    X.sort()
    min = 1000000
    for i in range(X[0], X[N-1]+1):
        sum = 0
        for j in range(N):
            sum += (X[j]-i)**2
        if sum < min:
            min = sum
    print(min)
