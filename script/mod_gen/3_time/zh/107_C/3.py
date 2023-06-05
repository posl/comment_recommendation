def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    time = 10**9
    for i in range(N-K+1):
        time = min(time, min(abs(x[i])+x[i+K-1]-x[i], abs(x[i+K-1])+x[i+K-1]-x[i]))
    print(time)

if __name__ == '__main__':
    main()