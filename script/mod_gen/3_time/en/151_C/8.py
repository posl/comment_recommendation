def main():
    # Read input
    N, M = map(int, input().split())
    p = []
    S = []
    for i in range(M):
        p_i, S_i = input().split()
        p.append(int(p_i))
        S.append(S_i)
    # Write output
    print(solve(N, M, p, S))

if __name__ == '__main__':
    main()