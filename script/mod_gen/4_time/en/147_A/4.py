def main():
    a = [int(x) for x in input().split()]
    if sum(a) >= 22:
        print('bust')
    else:
        print('win')

if __name__ == '__main__':
    main()