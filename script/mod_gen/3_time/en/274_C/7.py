def main():
    N = int(input())
    A = list(map(int,input().split()))
    d = {1:0}
    for i in range(1,N+1):
        d[2*i] = d[A[i-1]] + 1
        d[2*i+1] = d[A[i-1]] + 1
    for i in range(2**N):
        print(d[i+1])

if __name__ == '__main__':
    main()