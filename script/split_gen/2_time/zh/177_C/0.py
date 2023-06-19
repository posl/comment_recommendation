def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n-1):
        for j in range(i+1, n):
            sum += a[i] * a[j]
    print(sum % (10**9 + 7))
