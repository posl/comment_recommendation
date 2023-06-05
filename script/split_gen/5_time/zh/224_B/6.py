def main():
    h,w = map(int,input().split())
    A = [list(map(int,input().split())) for i in range(h)]
    #print(A)
    for i in range(h):
        for j in range(w):
            for k in range(i+1,h):
                for l in range(j+1,w):
                    #print(i,j,k,l)
                    if (A[i][j]+A[k][l])>(A[i][l]+A[k][j]):
                        print("No")
                        return
    print("Yes")
    return
main()
