def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    maxsum = 0
    for i in range(k):
        maxsum += p[i]
    sum = maxsum
    for i in range(k,n):
        sum = sum - p[i-k] + p[i]
        if sum > maxsum:
            maxsum = sum
    print((maxsum + k)/2)
