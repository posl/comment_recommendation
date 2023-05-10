def main():
    N,A,B = map(int,input().split())
    for i in range(A*N):
        for j in range(B*N):
            if (j//B+i//A)%2==0:
                print(".",end="")
            else:
                print("#",end="")
        print("")
