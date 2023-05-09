def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for i in range(N)]
    R = [sum(P[i]) for i in range(N)]
    R.sort(reverse=True)
    print("Yes" if R[K-1] > R[K] else "No")

if __name__ == '__main__':
    main()