def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    #print(A)
    ans = 0
    i = 0
    while i < N:
        if i == N-1:
            ans += 1
            break
        if A[i] == A[i+1]:
            i += 2
            ans += 1
        else:
            i += 1
    print(ans)

if __name__ == '__main__':
    main()