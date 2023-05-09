def main():
    N = int(input())
    H = list(map(int, input().split()))
    M = [0] * N
    M[0] = H[0]
    for i in range(1, N):
        M[i] = max(M[i-1], H[i])
    print(sum([1 for i in range(N) if M[i] == H[i]]))

if __name__ == '__main__':
    main()