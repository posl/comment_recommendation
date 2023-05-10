def main():
    # input
    A_1, A_2, A_3 = map(int, input().split())
    # compute
    # output
    print(max(A_1, A_2, A_3) - min(A_1, A_2, A_3))
