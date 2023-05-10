def main():
    N = input()
    if len(N) == 1:
        if int(N) % 3 == 0:
            print(0)
        else:
            print(-1)
    else:
        N = [int(i) for i in N]
        N.sort()
        N = N[::-1]
        sumN = sum(N)
        if sumN % 3 == 0:
            print(0)
        else:
            if sumN % 3 == 1:
                if 1 in N:
                    N.remove(1)
                    if sum(N) % 3 == 0:
                        print(1)
                    else:
                        if 2 in N:
                            N.remove(2)
                            if sum(N) % 3 == 0:
                                print(2)
                            else:
                                print(-1)
                        else:
                            print(-1)
                else:
                    if 2 in N:
                        N.remove(2)
                        if sum(N) % 3 == 0:
                            print(2)
                        else:
                            print(-1)
                    else:
                        print(-1)
            elif sumN % 3 == 2:
                if 2 in N:
                    N.remove(2)
                    if sum(N) % 3 == 0:
                        print(1)
                    else:
                        if 1 in N:
                            N.remove(1)
                            if sum(N) % 3 == 0:
                                print(2)
                            else:
                                print(-1)
                        else:
                            print(-1)
                else:
                    if 1 in N:
                        N.remove(1)
                        if sum(N) % 3 == 0:
                            print(2)
                        else:
                            print(-1)
                    else:
                        print(-1)
            else:
                print(-1)
