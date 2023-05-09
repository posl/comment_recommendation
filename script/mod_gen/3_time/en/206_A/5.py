def main():
    N = int(input())
    tax = N * 1.08
    if tax < 206:
        print('Yay!')
    elif tax == 206:
        print('so-so')
    else:
        print(':(')
main()

if __name__ == '__main__':
    main()