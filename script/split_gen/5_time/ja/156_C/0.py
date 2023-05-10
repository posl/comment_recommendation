def main():
    N = int(input())
    X = list(map(int, input().split()))
    min_sum = 10000000000000000
    for i in range(1, 101):
        sum = 0
        for j in range(N):
            sum += (X[j] - i) ** 2
        if sum < min_sum:
            min_sum = sum
    print(min_sum)
