def main():
    N = int(input())
    A = list(map(int, input().split()))
    parent = [0] * (2 * N + 1)
    for i in range(N):
        parent[2 * i + 1] = A[i]
        parent[2 * i + 2] = A[i]
    for i in range(2 * N + 1):
        if parent[i] == 0:
            print(0)
        else:
            count = 1
            while parent[i] != 1:
                parent[i] = parent[parent[i]]
                count += 1
            print(count)
