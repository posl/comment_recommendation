def main():
    # read input
    N = int(input())
    # write output
    if N <= 54:
        print('AGC' + str(N).zfill(3))
    else:
        print('AGC' + str(N + 1).zfill(3))
main()
