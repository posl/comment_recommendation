def main():
    N = int(input())
    tax = int(N * 1.08)
    if tax < 206:
        print('Yay!')
    elif tax == 206:
        print('so-so')
    else:
        print(':(')

if __name__ == '__main__':
    main()