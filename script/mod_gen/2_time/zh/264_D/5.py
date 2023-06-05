def main():
    h1,w1 = map(int,input().split())
    A = []
    for i in range(h1):
        A.append(list(map(int,input().split())))
    h2,w2 = map(int,input().split())
    B = []
    for i in range(h2):
        B.append(list(map(int,input().split())))
    #print(A)
    #print(B)
    if h1 < h2 or w1 < w2:
        print("No")
        return
    for i in range(h1-h2+1):
        for j in range(w1-w2+1):
            #print("i:{},j:{}".format(i,j))
            #print(A[i][j:j+w2])
            #print(B[0])
            if A[i][j:j+w2] == B[0]:
                #print("A[i][j:j+w2]:{}".format(A[i][j:j+w2]))
                #print("B[0]:{}".format(B[0]))
                #print("A[i][j:j+w2] == B[0]:{}".format(A[i][j:j+w2] == B[0]))
                for k in range(1,h2):
                    #print("A[i+k][j:j+w2]:{}".format(A[i+k][j:j+w2]))
                    #print("B[k]:{}".format(B[k]))
                    #print("A[i+k][j:j+w2] == B[k]:{}".format(A[i+k][j:j+w2] == B[k]))
                    if A[i+k][j:j+w2] != B[k]:
                        break
                else:
                    print("Yes")
                    return
    print("No")
    return

if __name__ == '__main__':
    main()