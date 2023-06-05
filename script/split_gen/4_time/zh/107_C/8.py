def main():
    n,k = map(int, input().split())
    x = list(map(int, input().split()))
    
    min_time = 10**9
    for i in range(n-k+1):
        if x[i] <= 0 and x[i+k-1] >= 0:
            min_time = min(min_time, abs(x[i])+abs(x[i]-x[i+k-1]), abs(x[i+k-1])+abs(x[i]-x[i+k-1]))
        elif x[i] <= 0 and x[i+k-1] <= 0:
            min_time = min(min_time, abs(x[i]))
        else:
            min_time = min(min_time, abs(x[i+k-1]))
    print(min_time)
