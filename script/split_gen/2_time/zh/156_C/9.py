def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    min = 100000
    for i in range(x[0], x[-1]+1):
        sum = 0
        for j in range(n):
            sum += (x[j] - i) ** 2
        if sum < min:
            min = sum
    print(min)
