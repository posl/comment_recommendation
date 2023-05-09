def main():
    #S, T, A, B, U = input().split()
    #A = int(A)
    #B = int(B)
    #print(A-1, B)
    
    S, T = input().split()
    A, B = input().split()
    U = input()
    if U == S:
        print(int(A)-1, B)
    else:
        print(A, int(B)-1)

if __name__ == '__main__':
    main()