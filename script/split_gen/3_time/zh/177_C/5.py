def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    sum = 0
    for i in range(n):
        for j in range(i+1,n):
            sum = (sum + a[i]*a[j])%(10**9+7)
    print(sum)
