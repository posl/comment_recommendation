def main():
    # input
    A, B = map(int, input().split())
    # compute
    # output
    if A+B < 10**10:
        print('Easy')
    else:
        print('Hard')
