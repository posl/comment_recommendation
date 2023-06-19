def main():
    print("start")
    #H,W,C = map(int,input().split())
    #print(H,W,C)
    #A = []
    #for i in range(H):
    #    A.append(list(map(int,input().split())))
    #print(A)
    H,W,C = 3,4,2
    A = [[1,7,7,9],[9,6,3,7],[7,8,6,4]]
    print(A)
    #H,W,C = 3,3,1000000000
    #A = [[1000000,1000000,1],[1000000,1000000,1000000],[1,1000000,1000000]]
    #print(A)
    #print("end")
    print("start")
    print(H,W,C)
    print(A)
    print("end")
    min_cost = 10**9
    for i in range(H):
        for j in range(W):
            for k in range(i,H):
                for l in range(j,W):
                    if i==k and j==l:
                        continue
                    cost = A[i][j] + A[k][l] + C*((i-k)**2 + (j-l)**2)
                    print(i,j,k,l,cost)
                    min_cost = min(min_cost,cost)
    print(min_cost)

if __name__ == '__main__':
    main()