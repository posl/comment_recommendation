def main():
    N, K, D = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    #print(N, K, D, a)
    if K == 1:
        if a[0] % D == 0:
            print(a[0])
        else:
            print(-1)
    elif K == N:
        if a[-1] % D == 0:
            print(a[-1])
        else:
            print(-1)
    else:
        #a[0]からa[N-1]までの間にDの倍数があるかどうか
        if a[0] % D == 0 or a[-1] % D == 0:
            print(a[-1])
        else:
            #a[0]からa[N-1]までの間にDの倍数があるかどうか
            if a[0] // D == a[-1] // D:
                print(-1)
            else:
                #a[0]からa[N-1]までの間にDの倍数があるかどうか
                if a[0] // D == a[-1] // D - 1:
                    if (a[-1] - a[0]) % D == 0:
                        print(-1)
                    else:
                        print(a[-1])
                else:
                    #a[0]からa[N-1]までの間にDの倍数があるかどうか
                    if a[0] // D == a[-1] // D - 2:
                        if (a[-1] - a[0]) % D == 0:
                            print(-1)
                        else:
                            print(a[-1])
                    else:
                        print(-1)
