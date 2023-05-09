def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, A, Q, BC)
    
    # Aの要素の値がBであるものの個数を記録
    count = [0] * (10**5 + 1)
    for a in A:
        count[a] += 1
    
    # S_{i}を記録
    S = [0] * (Q+1)
    S[0] = sum(A)
    for i in range(Q):
        B, C = BC[i]
        S[i+1] = S[i] - B * count[B] + C * count[B]
        count[C] += count[B]
        count[B] = 0
        print(S[i+1])

if __name__ == '__main__':
    main()