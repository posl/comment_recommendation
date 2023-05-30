def main():
    # read input
    A, B = input().split()
    # compute
    A = int(A)
    B = float(B)
    C = A * B
    # truncate
    C = int(C)
    # print result
    print(C)
main()
