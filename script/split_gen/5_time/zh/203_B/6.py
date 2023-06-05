def main():
    n, k = map(int, input().split())
    sum = 0
    for i in range(n):
        for j in range(k):
            sum += (i + 1) * 100 + (j + 1)
    print(sum)
