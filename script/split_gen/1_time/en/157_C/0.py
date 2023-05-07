def main():
    N, M = map(int, input().split())
    S = [0] * M
    C = [0] * M
    for i in range(M):
        S[i], C[i] = map(int, input().split())
    if N == 1:
        if M == 0:
            print(0)
        elif M == 1:
            print(C[0])
        else:
            print(-1)
    elif N == 2:
        if M == 0:
            print(10, 99)
        elif M == 1:
            if S[0] == 1:
                print(C[0] * 10, C[0] * 10 + 9)
            else:
                print(10 + C[0], 19 + C[0])
        elif M == 2:
            if S[0] == 1 and S[1] == 2:
                print(C[0] * 10 + C[1], C[0] * 10 + C[1])
            else:
                print(-1)
        else:
            print(-1)
    else:  # N == 3
        if M == 0:
            print(100, 999)
        elif M == 1:
            if S[0] == 1:
                print(C[0] * 100, C[0] * 100 + 99)
            elif S[0] == 2:
                print(100 + C[0] * 10, 199 + C[0] * 10)
            else:
                print(100 + C[0], 199 + C[0])
        elif M == 2:
            if S[0] == 1 and S[1] == 2:
                print(C[0] * 100 + C[1] * 10, C[0] * 100 + C[1] * 10 + 9)
            elif S[0] == 1 and S[1] == 3:
                print(C[0] * 100 + C[1], C[0] * 100 + C[1] + 9)
            elif S[0] == 2 and S[1] == 3:
                print(100 + C[0] * 10 + C[1
