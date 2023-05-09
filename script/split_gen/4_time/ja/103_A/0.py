def main():
    # input
    A1, A2, A3 = map(int, input().split())
    # compute
    # output
    print(min(abs(A1-A2)+abs(A2-A3), abs(A1-A3)+abs(A3-A2), abs(A2-A1)+abs(A1-A3)))
