def main():
    N,K = map(int,input().split())
    x = list(map(int,input().split()))
    min_time = 10**9
    for i in range(N-K+1):
        left = x[i]
        right = x[i+K-1]
        if left*right < 0:
            time = abs(left) + right - left
        else:
            time = max(abs(left),abs(right))
        if min_time > time:
            min_time = time
    print(min_time)

if __name__ == '__main__':
    main()