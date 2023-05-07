def main():
    N = int(input())
    A = list()
    B = list()
    for i in range(N-1):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(len(A))
    #print(len(B))
    visited = [0] * N
    visited[0] = 1
    #print(visited)
    route = [1]
    #print(route)
    for i in range(N-1):
        if B[i] == route[-1]:
            route.append(A[i])
        elif A[i] == route[-1]:
            route.append(B[i])
        else:
            continue
    #print(route)
    route.append(1)
    print(*route)

if __name__ == '__main__':
    main()