def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    #print(N, A)
    B = sorted(A)
    #print(B)
    C = B[-2]
    #print(C)
    print(A.index(C)+1)
main()

if __name__ == '__main__':
    main()