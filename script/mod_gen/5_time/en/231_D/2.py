def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #print(A)
    #print(B)
    A = sorted(A)
    B = sorted(B)
    #print(A)
    #print(B)
    if A[M-1] < B[0]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()