def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B2C = {}
    for i in range(N):
        if B[i] in B2C:
            B2C[B[i]].append(C[i])
        else:
            B2C[B[i]] = [C[i]]
    ans = 0
    for i in range(N):
        if A[i] in B2C:
            ans += len(B2C[A[i]])
    print(ans)

if __name__ == '__main__':
    main()