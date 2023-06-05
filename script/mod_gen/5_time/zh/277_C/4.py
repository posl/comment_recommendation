def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #A.sort()
    #B.sort()
    #print(A)
    #print(B)
    if N == 1:
        print(max(A[0], B[0]))
        return
    A.sort()
    B.sort()
    #print(A)
    #print(B)
    if N % 2 == 1:
        print(max(A[N//2], B[N//2]))
    else:
        print(max(A[N//2-1], B[N//2-1], A[N//2], B[N//2]))

if __name__ == '__main__':
    main()