def dice(n,k,p):
    max_sum = 0
    for i in range(0, n-k+1):
        sum = 0
        for j in range(i, i+k):
            sum += p[j]
        max_sum = max(max_sum, sum)
    return max_sum/2.0
n, k = map(int, input().split())
p = list(map(int, input().split()))
print(dice(n,k,p))

if __name__ == '__main__':
    dice()