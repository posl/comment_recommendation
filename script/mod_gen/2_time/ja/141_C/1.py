def main():
    N, K, Q = map(int, input().split())
    point = [K] * N
    for _ in range(Q):
        point[int(input()) - 1] += 1
    for p in point:
        print("Yes" if p > Q else "No")

if __name__ == '__main__':
    main()