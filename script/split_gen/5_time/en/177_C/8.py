def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(n)
    #print(a)
    sum = 0
    for i in range(n-1):
        for j in range(i+1,n):
            sum += a[i] * a[j]
            sum %= (10**9+7)
    print(sum)
