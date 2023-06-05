def main():
    #input
    N, M = map(int, input().split())
    #calc
    ans = N * (N - 1) // 2 + M * (M - 1) // 2
    #output
    print(ans)

if __name__ == '__main__':
    main()