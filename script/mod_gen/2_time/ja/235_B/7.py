def main():
    N = int(input())
    H = list(map(int,input().split()))
    #print(N)
    #print(H)
    H_max = H[0]
    for i in range(1,N):
        if H[i-1] <= H[i]:
            H_max = H[i]
    print(H_max)

if __name__ == '__main__':
    main()