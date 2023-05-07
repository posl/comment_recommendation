def main():
    #read input
    X = int(input())
    #check if X is divisible by 100
    if X % 100 == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()