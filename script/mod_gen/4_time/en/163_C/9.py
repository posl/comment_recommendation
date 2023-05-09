def main():
    n=int(input())
    A=list(map(int,input().split()))
    B=[0]*n
    for i in range(len(A)):
        B[A[i]-1]+=1
    for i in range(len(B)):
        print(B[i])

if __name__ == '__main__':
    main()