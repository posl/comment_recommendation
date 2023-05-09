def main():
    # input
    N = int(input())
    # compute
    price = int(N*1.08)
    # output
    if price < 206:
        print('Yay!')
    elif price == 206:
        print('so-so')
    else:
        print(':(')
