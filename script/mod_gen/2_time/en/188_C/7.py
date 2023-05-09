def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    A = sorted(A)
    #print(A)
    print(A[1])

if __name__ == '__main__':
    main()