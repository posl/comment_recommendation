def main():
    N = input()
    N = list(N)
    N = [int(i) for i in N]
    N = sorted(N)
    N = [str(i) for i in N]
    N = ''.join(N)
    N = int(N)
    if N % 3 == 0:
        print(0)
    elif N % 3 == 1:
        if len(N) == 1:
            print(-1)
        else:
            for i in range(len(N)):
                if int(N[i]) % 3 == 1:
                    print(1)
                    break
                elif int(N[i]) % 3 == 2 and len(N) > 2:
                    print(2)
                    break
                elif int(N[i]) % 3 == 2 and len(N) == 2:
                    print(-1)
                    break
    else:
        if len(N) == 1:
            print(-1)
        else:
            for i in range(len(N)):
                if int(N[i]) % 3 == 2:
                    print(1)
                    break
                elif int(N[i]) % 3 == 1 and len(N) > 2:
                    print(2)
                    break
                elif int(N[i]) % 3 == 1 and len(N) == 2:
                    print(-1)
                    break
