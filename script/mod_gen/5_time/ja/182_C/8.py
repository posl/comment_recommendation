def main():
    N = input()
    if len(N) == 1:
        if int(N) % 3 == 0:
            print(0)
            return
        else:
            print(-1)
            return
    else:
        N = [int(i) for i in N]
        N.sort()
        N.reverse()
        #print(N)
        sum = 0
        for i in range(len(N)):
            sum += N[i]
        if sum % 3 == 0:
            print(0)
            return
        else:
            if len(N) == 2:
                print(-1)
                return
            else:
                if sum % 3 == 1:
                    if N[-1] % 3 == 1:
                        print(1)
                        return
                    elif N[-1] % 3 == 2:
                        if len(N) == 3:
                            print(-1)
                            return
                        else:
                            if N[-2] % 3 == 2:
                                print(2)
                                return
                            else:
                                print(1)
                                return
                    else:
                        if len(N) == 3:
                            print(-1)
                            return
                        else:
                            if N[-2] % 3 == 2:
                                print(1)
                                return
                            else:
                                print(2)
                                return
                else:
                    if N[-1] % 3 == 2:
                        print(1)
                        return
                    elif N[-1] % 3 == 1:
                        if len(N) == 3:
                            print(-1)
                            return
                        else:
                            if N[-2] % 3 == 1:
                                print(2)
                                return
                            else:
                                print(1)
                                return
                    else:
                        if len(N) == 3:
                            print(-1)
                            return
                        else:
                            if N[-2] % 3 == 1:
                                print(1)
                                return
                            else:
                                print(2)
                                return

if __name__ == '__main__':
    main()