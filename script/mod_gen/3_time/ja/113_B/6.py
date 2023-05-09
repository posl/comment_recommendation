def main():
    N = int(input())
    T,A = map(int,input().split())
    H = list(map(int,input().split()))
    ans = 0
    min = 1000
    for i in range(N):
        if abs(A-(T-H[i]*0.006)) < min:
            ans = i+1
            min = abs(A-(T-H[i]*0.006))
    print(ans)

if __name__ == '__main__':
    main()