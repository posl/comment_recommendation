def main():
    N = input()
    n = len(N)
    if n == 1:
        if int(N)%3 == 0:
            print(0)
        else:
            print(-1)
    elif n == 2:
        if int(N)%3 == 0:
            print(0)
        else:
            print(1)
    else:
        N = list(N)
        N = [int(i) for i in N]
        sum_N = sum(N)
        if sum_N%3 == 0:
            print(0)
        else:
            if sum_N%3 == 1:
                if 1 in N:
                    if n == 3:
                        print(1)
                    else:
                        print(0)
                elif 4 in N:
                    if n == 3:
                        print(1)
                    else:
                        print(0)
                elif 7 in N:
                    if n == 3:
                        print(1)
                    else:
                        print(0)
                else:
                    if n <= 5:
                        print(2)
                    else:
                        print(1)
            else:
                if 2 in N:
                    if n == 3:
                        print(1)
                    else:
                        print(0)
                elif 5 in N:
                    if n == 3:
                        print(1)
                    else:
                        print(0)
                elif 8 in N:
                    if n == 3:
                        print(1)
                    else:
                        print(0)
                else:
                    if n <= 5:
                        print(2)
                    else:
                        print(1)

if __name__ == '__main__':
    main()