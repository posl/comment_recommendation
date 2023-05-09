def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i+1, 0)
    for i in range(1, N):
        print(i, i+1, 10**6)
    for i in range(1, N):
        for j in range(i+2, N+1):
            print(i, j, 10**6)
    for i in range(1, N):
        print(i, i+1, 10**6 - 1)
    for i in range(1, N):
        for j in range(i+2, N+1):
            print(i, j, 10**6 - 1)
    for i in range(1, N):
        for j in range(i+2, N+1):
            print(i, j, 10**6 - 2)
    for i in range(1, N):
        for j in range(i+2, N+1):
            print(i, j, 10**6 - 3)
    for i in range(1, N):
        for j in range(i+2, N+1):
            print(i, j, 10**6 - 4)
    for i in range(1, N):
        for j in range(i+2, N+1):
            print(i, j, 10**6 - 5)
    for i in range(1, N):
        for j in range(i+2, N+1):
            print(i, j, 10**6 - 6)
    for i in range(1, N):
        for j in range(i+2, N+1):
            print(i, j, 10**6 - 7)
    for i in range(1, N):
        for j in range(i+2, N+1):
            print(i, j, 10**6 - 8)
    for i in range(1, N):
        for j in range(i+2, N+1):
            print(i, j, 10**6 - 9)
    for i in range(1, N):
        for j in range(i+2, N+1):
            print(i, j, 10**6 - 10)
