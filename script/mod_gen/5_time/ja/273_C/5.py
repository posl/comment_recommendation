def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    A.sort()
    #print(A)
    K = 0
    for i in range(N):
        if i == 0:
            cnt = 1
        elif A[i] != A[i-1]:
            K += 1
            cnt = 1
        else:
            cnt += 1
        if i == N - 1:
            print(cnt)
        elif A[i] != A[i+1]:
            print(cnt)
    #print(K)
    #for i in range(N):
    #    print(K)

if __name__ == '__main__':
    main()