def  main():
    #input
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    #compute
    S = [list(s) for s in S]
    T = [list(t) for t in T]
    #output
    print('Yes' if solve(N, S, T) else 'No')
