def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    max = 0
    sum = 0
    for i in range(k):
        sum += p[i]
    max = sum
    for i in range(k,n):
        sum = sum + p[i] - p[i-k]
        if max < sum:
            max = sum
    print((max+k)/2)
