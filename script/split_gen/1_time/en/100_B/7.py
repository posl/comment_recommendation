def main():
    # Read the input
    D, N = list(map(int, input().split()))
    # Find the N-th smallest integer that can be divided by 100 exactly D times
    if N == 100:
        if D == 0:
            print(101)
        else:
            print(10100)
    else:
        if D == 0:
            print(N)
        elif D == 1:
            print(N*100)
        else:
            print(N*10000)
