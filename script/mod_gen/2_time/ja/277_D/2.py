def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * M
    for a in A:
        B[a] += 1
    #print(B)
    C = [0] * M
    for i in range(M):
        C[i] += B[i]
        if i + 1 < M:
            C[i + 1] += B[i]
        else:
            C[0] += B[i]
    #print(C)
    ans = 0
    for i in range(M):
        ans += i * (C[i] - B[i])
    print(ans)

if __name__ == '__main__':
    main()