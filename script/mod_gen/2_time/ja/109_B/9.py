def main():
    N = int(input())
    W = [input() for _ in range(N)]
    #print(W)
    for i in range(N):
        for j in range(i+1, N):
            #print(W[i], W[j])
            if W[i] == W[j]:
                print("No")
                return
    for i in range(N-1):
        if W[i][-1] != W[i+1][0]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()