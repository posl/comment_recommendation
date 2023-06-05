def main():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if A[M-1] < B[0]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()