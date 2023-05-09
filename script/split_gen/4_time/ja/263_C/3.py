def main():
    n,m = map(int,input().split())
    for i in range(1,m+1):
        if i > n:
            break
        else:
            for j in range(i+1,m+1):
                if j > n:
                    break
                else:
                    for k in range(j+1,m+1):
                        if k > n:
                            break
                        else:
                            print(i,j,k)
