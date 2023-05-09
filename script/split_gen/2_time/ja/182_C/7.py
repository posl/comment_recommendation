def main():
    N = input()
    N = list(N)
    N = [int(i) for i in N]
    N.sort()
    #print(N)
    if N[-1] == 0:
        print(0)
        exit()
    if sum(N) % 3 != 0:
        print(-1)
        exit()
    if N[0] == 0:
        for i in range(1,len(N)):
            if N[i] != 0:
                N[i],N[0] = N[0],N[i]
                print(len(N)-i)
                exit()
        print(-1)
        exit()
    print(0)
