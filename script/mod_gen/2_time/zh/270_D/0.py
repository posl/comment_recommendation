def main():
    N, X, Y = map(int, input().split())
    edges = []
    for i in range(N-1):
        U_i, V_i = map(int, input().split())
        edges.append([U_i, V_i])
    print(edges)

if __name__ == '__main__':
    main()