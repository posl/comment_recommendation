def main():
    N, M = map(int, input().split())
    S = [0] * M
    C = [0] * M
    for i in range(M):
        S[i], C[i] = map(int, input().split())
    if N == 1:
        if M == 0:
            print(0)
        else:
            if S[0] == 1:
                print(C[0])
            else:
                print(-1)
    else:
        if N == 2:
            for i in range(10):
                for j in range(10):
                    if (i * 10 + j) % (10 ** (N - S[0])) == C[0] * (10 ** (N - S[0])):
                        if M == 1:
                            print(i * 10 + j)
                        else:
                            for k in range(1, M):
                                if (i * 10 + j) % (10 ** (N - S[k])) == C[k] * (10 ** (N - S[k])):
                                    if k == M - 1:
                                        print(i * 10 + j)
                                else:
                                    break
        else:
            if N == 3:
                for i in range(10):
                    for j in range(10):
                        for k in range(10):
                            if (i * 100 + j * 10 + k) % (10 ** (N - S[0])) == C[0] * (10 ** (N - S[0])):
                                if M == 1:
                                    print(i * 100 + j * 10 + k)
                                else:
                                    for l in range(1, M):
                                        if (i * 100 + j * 10 + k) % (10 ** (N - S[l])) == C[l] * (10 ** (N - S[l])):
                                            if l == M - 1:
                                                print(i * 100 + j * 10 + k)
                                        else:
                                            break
            else:
                print(-1)
main()

if __name__ == '__main__':
    main()