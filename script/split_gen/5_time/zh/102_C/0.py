def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.append(a[i] - (i+1))
    b.sort()
    if n % 2 == 0:
        b1 = b[n//2]
        b2 = b[n//2 - 1]
        sum1 = 0
        sum2 = 0
        for i in range(n):
            sum1 += abs(b1 - b[i])
            sum2 += abs(b2 - b[i])
        print(min(sum1, sum2))
    else:
        b1 = b[n//2]
        sum1 = 0
        for i in range(n):
            sum1 += abs(b1 - b[i])
        print(sum1)
