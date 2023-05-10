def main():
    N = int(input())
    X = list(map(int, input().split()))
    result = float("inf")
    for i in range(1, 101):
        sum = 0
        for j in range(N):
            sum += (X[j] - i) ** 2
        result = min(result, sum)
    print(result)
