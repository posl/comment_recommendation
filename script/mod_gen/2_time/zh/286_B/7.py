def main():
    #get N,P,Q,R,S
    line = input()
    line = line.split()
    N = int(line[0])
    P = int(line[1])
    Q = int(line[2])
    R = int(line[3])
    S = int(line[4])
    #get A
    line = input()
    line = line.split()
    A = []
    for i in range(N):
        A.append(int(line[i]))
    #get B
    B = []
    for i in range(N):
        if i < P-1 or i > Q-1:
            B.append(A[i])
        else:
            B.append(A[i+R-Q])
    #print B
    for i in range(N):
        print(B[i], end=" ")

if __name__ == '__main__':
    main()