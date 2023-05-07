def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    points = [K-Q for _ in range(N)]
    for a in A:
        points[a-1] += 1
    for p in points:
        if p > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()