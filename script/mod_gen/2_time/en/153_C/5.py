def main():
    #input
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    #compute
    H.sort()
    ans = sum(H[:-K]) if N-K >= 0 else 0
    #output
    print(ans)

if __name__ == '__main__':
    main()