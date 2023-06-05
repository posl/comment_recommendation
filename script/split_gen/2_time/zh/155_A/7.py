def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    max_sum = 0
    for i in range(n-k+1):
        sum = 0
        for j in range(i,i+k):
            sum += p[j]
        if max_sum < sum:
            max_sum = sum
    print((max_sum+k)/2)
