def main():
    n = int(input())
    d = [int(i) for i in input().split()]
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += d[i] * d[j]
    print(sum)
