def readinput():
    line = input()
    N,M = line.split()
    N = int(N)
    M = int(M)
    switches = []
    for i in range(M):
        line = input()
        switch = list(map(int, line.split()))
        switches.append(switch)
    line = input()
    P = list(map(int, line.split()))
    return (N,M,switches,P)
