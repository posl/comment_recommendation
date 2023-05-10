def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    #print(N,A,B,C,D,E)
    #print(N//min(A,B,C,D,E) + 5)
    #print(N//min(A,B,C,D,E) + 5 if N%min(A,B,C,D,E) == 0 else N//min(A,B,C,D,E) + 6)
    print(N//min(A,B,C,D,E) + 5 if N%min(A,B,C,D,E) == 0 else N//min(A,B,C,D,E) + 6)

if __name__ == '__main__':
    main()