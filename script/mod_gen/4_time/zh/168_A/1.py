def main():
    n = int(input())
    if n%10 in [2,4,5,7,9]:
        print('hon')
    elif n%10 in [0,1,6,8]:
        print('pon')
    elif n%10 in [3]:
        print('bon')

if __name__ == '__main__':
    main()