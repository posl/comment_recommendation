def main():
    N = input()
    N = [int(i) for i in N]
    #print(N)
    N.sort()
    #print(N)
    #print(N[0])
    if N[0] == 0:
        print(-1)
        return
    if sum(N) % 3 == 0:
        print(0)
        return
    if N[0] == 5:
        print(1)
        return
    if len(N) == 1:
        print(-1)
        return
    if (N[0] + N[1]) % 3 == 0:
        print(2)
        return
    print(1)
    return
