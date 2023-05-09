def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    #print(N, A, B, C, D, E)
    #print(N//min(A,B,C,D,E) + 5)
    print(int(5 + (N-1)//min(A,B,C,D,E)))

if __name__ == '__main__':
    main()