def main():
    N = int(input())
    A = list(map(int, input().split()))
    A1 = A[:N//2]
    A2 = A[N//2:]
    A2.reverse()
    A2 = A2[:N//2]
    A = A1 + A2
    #print(A)
    A.sort()
    A1 = A[:N//2]
    A2 = A[N//2:]
    A2.reverse()
    A2 = A2[:N//2]
    A = A1 + A2
    #print(A)
    B = A1 + A2
    B.sort()
    #print(B)
    ans = 0
    for i in range(N):
        if B[i] != A[i]:
            ans += 1
    print(ans//2)

if __name__ == '__main__':
    main()