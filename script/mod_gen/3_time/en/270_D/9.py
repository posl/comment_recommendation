def main():
    #input
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #calculation
    #Takahashi's turn
    if N in A:
        print(N)
    else:
        for i in range(1, N+1):
            if i not in A:
                print(i-1)
                break

if __name__ == '__main__':
    main()