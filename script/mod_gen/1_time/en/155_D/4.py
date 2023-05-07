def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [a for a in A if a < 0]
    B = [a for a in A if a < 0]
    C = [a for a in A if a >= 0]
    if not B:
        if K % 2 == 0:
            print(C[(K // 2) - 1] * C[K // 2])
        else:
            print(C[K // 2] * C[K // 2])
    elif not C:
        if K % 2 == 0:
            print(B[-(K // 2)] * B[-(K // 2) - 1])
        else:
            print(B[-(K // 2) - 1] * B[-(K // 2) - 1])
    else:
        ans = []
        for i in range(len(B)):
            for j in range(len(C)):
                ans.append(B[i] * C[j])
        ans.sort()
        print(ans[K - 1])

if __name__ == '__main__':
    main()