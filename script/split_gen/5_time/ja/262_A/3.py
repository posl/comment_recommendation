def main():
    # input
    Y = int(input())
    # compute
    # output
    if Y%4 == 2:
        print(Y)
    else:
        print(Y+4-Y%4+2)
