def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    S = [0, 0, 0, 0]
    for i in range(N):
        S[0] += 1
        for j in range(4):
            if S[j] > 0:
                if j + A[i] < 4:
                    S[j + A[i]] += S[j]
                    S[j] = 0
                else:
                    P += S[j]
                    S[j] = 0
    print(P)

if __name__ == '__main__':
    main()