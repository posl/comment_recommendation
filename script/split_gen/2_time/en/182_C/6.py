def main():
    N = int(input())
    N = str(N)
    N = [int(i) for i in N]
    N = sorted(N)
    N = [str(i) for i in N]
    N = int("".join(N))
    if N % 3 == 0:
        print(0)
    elif N % 3 == 1:
        if len(str(N)) == 1:
            print(-1)
        elif len(str(N)) == 2:
            print(-1)
        else:
            if 1 in N:
                print(1)
            elif 4 in N:
                print(1)
            elif 7 in N:
                print(1)
            else:
                print(2)
    else:
        if len(str(N)) == 1:
            print(-1)
        elif len(str(N)) == 2:
            print(-1)
        else:
            if 2 in N:
                print(1)
            elif 5 in N:
                print(1)
            elif 8 in N:
                print(1)
            else:
                print(2)
