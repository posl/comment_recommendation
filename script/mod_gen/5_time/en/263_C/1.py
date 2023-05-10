def main():
    n,m = map(int,input().split())
    for i in range(1,m+1):
        if n==1:
            print(i)
        else:
            for j in range(1,m+1):
                if n==2:
                    print(i,j)
                else:
                    for k in range(1,m+1):
                        if n==3:
                            print(i,j,k)
                        else:
                            for l in range(1,m+1):
                                if n==4:
                                    print(i,j,k,l)
                                else:
                                    for o in range(1,m+1):
                                        if n==5:
                                            print(i,j,k,l,o)
                                        else:
                                            for p in range(1,m+1):
                                                if n==6:
                                                    print(i,j,k,l,o,p)
                                                else:
                                                    for q in range(1,m+1):
                                                        if n==7:
                                                            print(i,j,k,l,o,p,q)
                                                        else:
                                                            for r in range(1,m+1):
                                                                if n==8:
                                                                    print(i,j,k,l,o,p,q,r)
                                                                else:
                                                                    for s in range(1,m+1):
                                                                        if n==9:
                                                                            print(i,j,k,l,o,p,q,r,s)
                                                                        else:
                                                                            for t in range(1,m+1):
                                                                                if n==10:
                                                                                    print(i,j,k,l,o,p,q,r,s,t)

if __name__ == '__main__':
    main()