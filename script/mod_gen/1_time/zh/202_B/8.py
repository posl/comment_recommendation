def main():
    #S = input()
    S = '0601889'
    S = S[::-1]
    S = S.replace('0','a')
    S = S.replace('1','b')
    S = S.replace('9','c')
    S = S.replace('8','d')
    S = S.replace('6','e')
    S = S.replace('a','0')
    S = S.replace('b','1')
    S = S.replace('c','9')
    S = S.replace('d','8')
    S = S.replace('e','6')
    print(S)

if __name__ == '__main__':
    main()