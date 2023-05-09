def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(N-3):
        for y in range(x+1, N-2):
            for z in range(y+1, N-1):
                for w in range(z+1, N):
                    ans = max(ans, P*A[x]+Q*A[y]+R*A[z]+A[w])
    print(ans)

if __name__ == '__main__':
    main()