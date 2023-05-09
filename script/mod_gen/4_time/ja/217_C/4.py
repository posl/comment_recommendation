def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0]*N
    for i in range(N):
        Q[P[i]-1] = str(i+1)
    print(" ".join(Q))

if __name__ == '__main__':
    main()