def main():
    # input
    A_1, A_2, A_3 = map(int, input().split())
    # compute
    # output
    if A_1+A_2+A_3 >= 22:
        print('bust')
    else:
        print('win')
