def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    
    if N%2 == 0:
        #print(N//2)
        b = A[N//2] - 1
    else:
        #print(N//2)
        b = A[N//2]
    #print(b)
    ans = 0
    for i in range(N):
        ans += abs(A[i] - (b+i+1))
    print(ans)

if __name__ == '__main__':
    main()