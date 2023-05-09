def dice(n,k,p):
    sum = 0
    for i in range(0,k):
        sum += p[i]
    max = sum
    for i in range(k,n):
        sum += p[i]
        sum -= p[i-k]
        if sum > max:
            max = sum
    return max
n,k = map(int,input().split())
p = list(map(int,input().split()))
max = dice(n,k,p)
print((max+k)/2)

if __name__ == '__main__':
    dice()