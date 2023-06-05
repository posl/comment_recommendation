def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    time = float('inf')
    for i in range(n-k+1):
        if x[i]*x[i+k-1] < 0:
            t = min(abs(x[i]),abs(x[i+k-1]))*2 + max(abs(x[i]),abs(x[i+k-1]))
        else:
            t = max(abs(x[i]),abs(x[i+k-1]))
        if t < time:
            time = t
    print(time)

if __name__ == '__main__':
    main()