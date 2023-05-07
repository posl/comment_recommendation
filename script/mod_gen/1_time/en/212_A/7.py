def main():
    #get input
    A, B = map(int, input().split())
    #check conditions
    if A > 0 and B == 0:
        print('Gold')
    elif A == 0 and B > 0:
        print('Silver')
    else:
        print('Alloy')

if __name__ == '__main__':
    main()