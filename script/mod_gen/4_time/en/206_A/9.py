def main():
    #input
    N = int(input())
    #calculate
    tax = 1.08
    price = int(N * tax)
    #output
    if price < 206:
        print('Yay!')
    elif price == 206:
        print('so-so')
    else:
        print(':(')

if __name__ == '__main__':
    main()