def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A, reverse=True)
    A1 = A[0:2**(N-1)]
    A2 = A[2**(N-1):2**N]
    print(A.index(min(A1, key=lambda x:abs(x-A2[0])))+1)

if __name__ == '__main__':
    main()