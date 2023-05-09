def main():
    # input
    V, T, S, D = map(int, input().split())
    # compute
    # output
    print('Yes' if D/V < T or S < D/V else 'No')
