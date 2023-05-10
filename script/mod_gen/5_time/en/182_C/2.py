def main():
    N = input()
    N = list(N)
    N = [int(i) for i in N]
    N.sort()
    sumN = sum(N)
    if sumN%3 == 0:
        print(0)
    else:
        if sumN%3 == 1:
            if 1 in N:
                if len(N) == 1:
                    print(-1)
                else:
                    N.remove(1)
                    sumN = sum(N)
                    if sumN%3 == 0:
                        print(1)
                    else:
                        if 2 in N:
                            N.remove(2)
                            sumN = sum(N)
                            if sumN%3 == 0:
                                print(2)
                            else:
                                print(-1)
                        else:
                            print(-1)
            else:
                if 2 in N:
                    if len(N) == 1:
                        print(-1)
                    else:
                        N.remove(2)
                        sumN = sum(N)
                        if sumN%3 == 0:
                            print(1)
                        else:
                            if 1 in N:
                                N.remove(1)
                                sumN = sum(N)
                                if sumN%3 == 0:
                                    print(2)
                                else:
                                    print(-1)
                            else:
                                print(-1)
                else:
                    print(-1)
        else:
            if 2 in N:
                if len(N) == 1:
                    print(-1)
                else:
                    N.remove(2)
                    sumN = sum(N)
                    if sumN%3 == 0:
                        print(1)
                    else:
                        if 1 in N:
                            N.remove(1)
                            sumN = sum(N)
                            if sumN%3 == 0:
                                print(2)
                            else:
                                print(-1)
                        else:
                            print(-1)
            else:
                if 1 in N:
                    if len(N) == 1:
                        print(-1)
                    else:
                        N.remove(1)
                        sumN = sum(N)
                        if sumN%3 == 0:
                            print(1)
                        else:
                            if 2 in N:
                                N.remove(2)
                                sumN = sum(N)
                                if sumN%3 == 0:
                                    print(2)
                                else:
                                    print(-1)
                            else:

if __name__ == '__main__':
    main()