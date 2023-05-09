def main():
    n = int(input())
    w = list(map(int, input().split()))
    w.sort(reverse=True)
    sum1 = 0
    sum2 = 0
    for i in range(n):
        if i % 2 == 0:
            sum1 += w[i]
        else:
            sum2 += w[i]
    print(abs(sum1 - sum2))
