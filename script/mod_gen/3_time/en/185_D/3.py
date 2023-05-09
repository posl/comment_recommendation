def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = [A[0]-1]
    for i in range(M-1):
        B.append(A[i+1]-A[i]-1)
    B.append(N-A[-1])
    B = [b for b in B if b != 0]
    if len(B) == 0:
        print(0)
        return
    k = min(B)
    ans = 1
    for b in B:
        if b % k == 0:
            ans += b//k
        else:
            ans += b//k + 1
    print(ans)

if __name__ == '__main__':
    main()