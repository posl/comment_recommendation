def main():
    N, M = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(M)]
    S.sort(key=lambda x: x[0])
    if N == 1:
        if M == 0:
            print(0)
            return
        else:
            for s, c in S:
                if s == 1 and c == 0:
                    print(-1)
                    return
                else:
                    print(c)
                    return
    else:
        if M == 0:
            print(10**(N-1))
            return
        else:
            if S[0][0] == 1:
                if S[0][1] == 0:
                    print(-1)
                    return
                else:
                    if M == 1:
                        print(S[0][1]*10**(N-1))
                        return
                    else:
                        if S[1][0] == 2:
                            print(S[0][1]*10**(N-1)+S[1][1])
                            return
                        else:
                            print(S[0][1]*10**(N-1)+10**(N-2))
                            return
            else:
                print(S[0][1]*10**(N-1)+10**(N-2))
                return
