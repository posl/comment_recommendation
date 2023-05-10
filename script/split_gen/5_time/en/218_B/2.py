def main():
    # input
    P = list(map(int, input().split()))
    # compute
    # output
    print(''.join([chr(ord('a') + P[i] - 1) for i in range(26)]))
