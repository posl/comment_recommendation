def main():
    N, K, Q = map(int, input().split())
    #N, K, Q = 10, 13, 15
    #A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
    A = [int(input()) for _ in range(Q)]
    #print(N, K, Q)
    #print(A)
    point = [K - Q] * N
    #print(point)
    for i in range(Q):
        point[A[i] - 1] += 1
    #print(point)
    for i in range(N):
        if point[i] > 0:
            print("Yes")
        else:
            print("No")
