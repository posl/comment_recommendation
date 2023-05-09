def main():
    N, M = map(int, input().split())
    S = [0] * M
    C = [0] * M
    for i in range(M):
        S[i], C[i] = map(int, input().split())
    if N == 1:
        if M == 0:
            print(0)
            return
        else:
            if S[0] == 1:
                print(C[0])
                return
            else:
                print(-1)
                return
    elif N == 2:
        if M == 0:
            print(10)
            return
        elif M == 1:
            if S[0] == 1:
                print(C[0] * 10)
                return
            elif S[0] == 2:
                print(C[0] + 10)
                return
            else:
                print(-1)
                return
        else:
            if S[0] == 1:
                if S[1] == 2:
                    if C[0] == C[1]:
                        print(C[0] * 10 + C[1])
                        return
                    else:
                        print(-1)
                        return
                else:
                    print(-1)
                    return
            elif S[0] == 2:
                if S[1] == 1:
                    if C[0] == C[1]:
                        print(C[0] * 10 + C[1])
                        return
                    else:
                        print(-1)
                        return
                else:
                    print(-1)
                    return
            else:
                print(-1)
                return
    else:
        if M == 0:
            print(100)
            return
        elif M == 1:
            if S[0] == 1:
                print(C[0] * 100)
                return
            elif S[0] == 2:
                print(C[0] * 10 + 100)
                return
            elif S[0] == 3:
                print(C[0] + 100)
                return
            else:
                print(-1)
                return
        elif M == 2:
            if S[0] == 1:
                if S[1] == 2:
                    if S[2] == 3:
                        if C[0]
