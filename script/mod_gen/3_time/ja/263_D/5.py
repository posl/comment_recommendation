def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    #print(N, L, R)
    #print(A)
    #print(sum(A))
    #print(A[N//2])
    #print(A[N//2-1])
    if L >= 0:
        print(sum(A) + (N//2)*L)
    elif R <= 0:
        print(sum(A) + (N//2)*R)
    else:
        if A[N//2] >= 0:
            print(sum(A[:N//2]) + sum(A[N//2:]) + (N//2)*L)
        elif A[N//2-1] <= 0:
            print(sum(A[:N//2]) + sum(A[N//2:]) + (N//2)*R)
        else:
            print(sum(A[:N//2]) + sum(A[N//2:]) + (N//2)*L + (N//2)*R)

if __name__ == '__main__':
    main()