def main():
    #入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    
    #出力
    B = []
    for i in range(M+1):
        B.append(C[i+N] - sum([A[j]*C[i+j] for j in range(N)]))
    print(*B)

if __name__ == '__main__':
    main()