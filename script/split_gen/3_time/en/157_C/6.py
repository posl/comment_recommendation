def main():
    N, M = map(int, input().split())
    if M == 0:
        if N == 1:
            print(0)
            return
        else:
            print(10**(N-1))
            return
    else:
        S = [0]*M
        C = [0]*M
        for i in range(M):
            S[i], C[i] = map(int, input().split())
        if N == 1:
            if M == 1:
                print(C[0])
                return
            else:
                print(-1)
                return
        else:
            if M == 1:
                if S[0] == 1:
                    if C[0] == 0:
                        print(-1)
                        return
                    else:
                        print(str(C[0]) + str(0)*(N-1))
                        return
                else:
                    print(str(1) + str(C[0]) + str(0)*(N-2))
                    return
            else:
                if S[0] == 1:
                    if C[0] == 0:
                        print(-1)
                        return
                    else:
                        for i in range(1, M):
                            if S[i] == 1:
                                print(-1)
                                return
                else:
                    print(str(1) + str(C[0]) + str(0)*(N-2))
                    return
                for i in range(1, M):
                    if S[i] == 1:
                        print(-1)
                        return
                for i in range(1, M):
                    if S[i] == 1:
                        print(-1)
                        return
                for i in range(1, M):
                    if S[i] == 1:
                        print(-1)
                        return
                for i in range(1, M):
                    if S[i] == 1:
                        print(-1)
                        return
                for i in range(1, M):
                    if S[i] == 1:
                        print(-1)
                        return
                for i in range(1, M):
                    if S[i] == 1:
                        print(-1)
                        return
                for i in range(1, M):
                    if S[i] == 1:
                        print(-1)
                        return
                for i in range(1, M):
