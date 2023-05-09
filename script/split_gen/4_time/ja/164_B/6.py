def main():
    # input
    A, B, C, D = map(int, input().split())
    # compute
    # output
    if (C-1)//B < (A-1)//D:
        print('Yes')
    else:
        print('No')
