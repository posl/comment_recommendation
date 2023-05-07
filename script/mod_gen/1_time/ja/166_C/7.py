def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    #print(H)
    #print(AB)
    #print(N, M)
    #print(H)
    #print(AB)
    #print(N, M)
    #print(H)
    #print(AB)
    count = 0
    for i in range(0, N):
        #print("i:", i)
        for j in range(0, M):
            #print("j:", j)
            if AB[j][0] == i + 1:
                #print("AB[j][0] == i + 1", AB[j][0], i + 1)
                #print(H[i], H[AB[j][1] - 1])
                if H[i] <= H[AB[j][1] - 1]:
                    #print("H[i] <= H[AB[j][1] - 1]", H[i], H[AB[j][1] - 1])
                    break
            elif AB[j][1] == i + 1:
                #print("AB[j][1] == i + 1", AB[j][1], i + 1)
                #print(H[i], H[AB[j][0] - 1])
                if H[i] <= H[AB[j][0] - 1]:
                    #print("H[i] <= H[AB[j][0] - 1]", H[i], H[AB[j][0] - 1])
                    break
            if j == M - 1:
                count += 1
    print(count)

if __name__ == '__main__':
    main()