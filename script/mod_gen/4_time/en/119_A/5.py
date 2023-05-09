def main():
    S = input()
    y, m, d = map(int, S.split('/'))
    if m <= 4:
        print('Heisei')
    else:
        print('TBD')

if __name__ == '__main__':
    main()