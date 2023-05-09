def main():
    N = int(input())
    A = list(map(int, input().split()))
    parent = [0] * (2*N+1)
    for i in range(N):
        a = A[i]
        parent[2*i+1] = a
        parent[2*i+2] = a
    for i in range(2*N+1):
        if parent[i] == 0:
            break
        parent[i] = parent[parent[i]-1]
    for i in range(2*N+1):
        print(parent[i])

if __name__ == '__main__':
    main()