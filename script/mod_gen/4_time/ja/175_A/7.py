def main():
    S = input()
    S = S.replace('S', '0')
    S = S.replace('R', '1')
    S = S.replace('01', '0,1')
    S = S.replace('10', '1,0')
    S = S.replace('00', '0,0')
    S = S.replace('11', '1,1')
    S = S.split(',')
    print(max(map(len, S)))

if __name__ == '__main__':
    main()