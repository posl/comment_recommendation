def main():
    line1 = input().split()
    line2 = input().split()
    N = int(line1[0])
    X = int(line1[1])
    A = list(map(int,line2))
    #print(N,X,A)
    #A[X-1] = 0
    #print(A)
    #count = 0
    #for i in range(N-1):
    #    if A[i] == i+1:
    #        if A[i+1] == i+2:
    #            count += 1
    #            A[i+1] = 0
    #print(count)
    count = 1
    x = X-1
    while True:
        #print(x)
        if A[x] == 0:
            break
        else:
            count += 1
            x = A[x]-1
    print(count)

if __name__ == '__main__':
    main()