def main():
    #input
    n = int(input())
    a = list(map(int,input().split()))
    #count
    count = [0] * (10**9+1)
    for i in range(n):
        count[a[i]] += 1
    #cumsum
    cumsum = [0] * (10**9+1)
    for i in range(10**9+1):
        cumsum[i] = cumsum[i-1] + count[i]
    #solve
    for i in range(n):
        print(n - cumsum[a[i]])
