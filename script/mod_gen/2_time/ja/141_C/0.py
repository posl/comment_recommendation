def main():
    N, K, Q = map(int, input().split())
    point = [K] * N
    for _ in range(Q):
        A = int(input())
        point[A-1] += 1
    for i in range(N):
        point[i] -= Q
        if point[i] > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()