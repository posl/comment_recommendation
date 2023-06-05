def main():
    N,L = map(int,input().split())
    sum = 0
    min = 1000
    for i in range(1,N+1):
        sum += L+i-1
        if abs(L+i-1) < abs(min):
            min = L+i-1
    print(sum-min)
