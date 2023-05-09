def main():
    #input
    N = int(input())
    S = [input() for _ in range(N)]
    #compute
    ans = 2**(N+1) - 2**(N+1-N)
    #output
    print(ans)
main()
