def main():
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    if N == 1:
        if S[0] in T:
            print(-1)
        else:
            print(S[0])
        return
    if N == 2:
        for i in range(1, 16):
            for j in range(1, 16):
                if i + j + len(S[0]) + len(S[1]) == 16:
                    X = S[0] + "_" * i + S[1] + "_" * j
                    if X not in T:
                        print(X)
                        return
        print(-1)
        return
    if N == 3:
        for i in range(1, 16):
            for j in range(1, 16):
                for k in range(1, 16):
                    if i + j + k + len(S[0]) + len(S[1]) + len(S[2]) == 16:
                        X = S[0] + "_" * i + S[1] + "_" * j + S[2] + "_" * k
                        if X not in T:
                            print(X)
                            return
        print(-1)
        return
    if N == 4:
        for i in range(1, 16):
            for j in range(1, 16):
                for k in range(1, 16):
                    for l in range(1, 16):
                        if i + j + k + l + len(S[0]) + len(S[1]) + len(S[2]) + len(S[3]) == 16:
                            X = S[0] + "_" * i + S[1] + "_" * j + S[2] + "_" * k + S[3] + "_" * l
                            if X not in T:
                                print(X)
                                return
        print(-1)
        return
    if N == 5:
        for i in range(1, 16):
            for j in range(1, 16):
                for k in range(1, 16):
                    for l in range(1, 16):
                        for m in range(1, 16):
                            if i +
