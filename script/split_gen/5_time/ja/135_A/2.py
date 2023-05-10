def main():
    # input
    A, B = map(int, input().split())
    # compute
    # output
    if (A+B)%2 == 0:
        print((A+B)//2)
    else:
        print("IMPOSSIBLE")
