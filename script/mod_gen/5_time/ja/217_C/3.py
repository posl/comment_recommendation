def main():
    N = int(input())
    P = []
    P = list(map(int, input().split()))
    Q = [0]*N
    for i in range(N):
        Q[P[i]-1] = i+1
    print(*Q)
    return

if __name__ == '__main__':
    main()