def main():
    # read input
    N, M = map(int, input().split())
    # calculate
    if N == 0:
        print(M)
    elif M == 0:
        print(N)
    else:
        print(N * M)
