def main():
    # input
    N = int(input())
    # compute
    # output
    if int(N*1.08) < 206:
        print('Yay!')
    elif int(N*1.08) == 206:
        print('so-so')
    else:
        print(':(')
