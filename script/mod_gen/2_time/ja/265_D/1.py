def main():
    N,P,Q,R = map(int,input().split())
    A = list(map(int,input().split()))
    ans = "No"
    for i in range(N-3):
        for j in range(i+1,N-2):
            for k in range(j+1,N-1):
                if P == sum(A[i:j]) and Q == sum(A[j:k]) and R == sum(A[k:]):
                    ans = "Yes"
    print(ans)

if __name__ == '__main__':
    main()