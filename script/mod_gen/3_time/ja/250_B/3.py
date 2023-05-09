def main():
    N,A,B = map(int,input().split())
    for i in range(A*N):
        for j in range(B*N):
            if (i//A + j//B)%2 == 0:
                print(".",end="")
            else:
                print("#",end="")
        print()

if __name__ == '__main__':
    main()