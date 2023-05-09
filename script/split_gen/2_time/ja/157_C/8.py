def main():
    N, M = map(int, input().split())
    s_c = [list(map(int, input().split())) for _ in range(M)]
    if N == 1:
        if M == 0:
            print(0)
        else:
            if s_c[0][1] == 0:
                print(-1)
            else:
                print(s_c[0][1])
    else:
        if M == 0:
            print(10 ** (N - 1))
        else:
            if N == 2:
                if s_c[0][0] == 1:
                    if s_c[0][1] == 0:
                        print(-1)
                    else:
                        print(10 * s_c[0][1])
                else:
                    print(s_c[0][1] * 10 + 10 ** (N - 1))
            else:
                if s_c[0][0] == 1:
                    if s_c[0][1] == 0:
                        print(-1)
                    else:
                        print(100 * s_c[0][1] + 10 ** (N - 1))
                elif s_c[0][0] == 2:
                    if s_c[0][1] == 0:
                        print(-1)
                    else:
                        print(10 * s_c[0][1] + 10 ** (N - 1))
                else:
                    print(s_c[0][1] * 100 + 10 ** (N - 1))
