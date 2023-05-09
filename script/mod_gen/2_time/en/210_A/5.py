def main():
    #get input
    N,A,X,Y = map(int,input().split())
    #calculate cost
    if N <= A:
        cost = N*X
    else:
        cost = A*X + (N-A)*Y
    #print cost
    print(cost)

if __name__ == '__main__':
    main()