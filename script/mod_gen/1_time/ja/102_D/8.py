def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 10**9
    # 1つ目の切り口
    for i in range(N-3):
        # 2つ目の切り口
        for j in range(i+1,N-2):
            # 3つ目の切り口
            for k in range(j+1,N-1):
                B = A[:i+1]
                C = A[i+1:j+1]
                D = A[j+1:k+1]
                E = A[k+1:]
                P = sum(B)
                Q = sum(C)
                R = sum(D)
                S = sum(E)
                ans = min(ans, max(P,Q,R,S)-min(P,Q,R,S))
    print(ans)

if __name__ == '__main__':
    main()