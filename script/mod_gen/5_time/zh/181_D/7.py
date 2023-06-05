def main():
    S = input()
    S = list(S)
    S.sort()
    S.reverse()
    S = ''.join(S)
    if int(S) % 8 == 0:
        print('是')
    else:
        print('否')

if __name__ == '__main__':
    main()