def main():
    #input
    NMXY = input().split()
    x = input().split()
    y = input().split()
    N = int(NMXY[0])
    M = int(NMXY[1])
    X = int(NMXY[2])
    Y = int(NMXY[3])
    #compute
    x.sort()
    y.sort()
    x = list(map(int, x))
    y = list(map(int, y))
    if x[N-1] < y[0] and X < y[0] and x[N-1] < Y:
        print('No War')
    else:
        print('War')
    #output
