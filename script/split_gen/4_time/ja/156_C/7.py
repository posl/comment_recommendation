def main():
    N = int(input())
    X = list(map(int, input().split()))
    min = 1000000000
    for i in range(1,100):
        sum = 0
        for j in range(N):
            sum += (X[j] - i)**2
        if sum < min:
            min = sum
    print(min)
