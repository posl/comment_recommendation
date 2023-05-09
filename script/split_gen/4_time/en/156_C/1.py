def main():
    n = int(input())
    x = list(map(int, input().split()))
    min_sum = 10000000
    for i in range(1, 101):
        sum = 0
        for j in range(n):
            sum += (x[j] - i)**2
        if sum < min_sum:
            min_sum = sum
    print(min_sum)
