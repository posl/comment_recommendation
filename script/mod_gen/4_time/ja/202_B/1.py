def main():
    S = input()
    S = S[::-1]
    S = S.replace('6','x')
    S = S.replace('9','6')
    S = S.replace('x','9')
    S = S.replace('0','x')
    S = S.replace('1','0')
    S = S.replace('x','1')
    print(S)
main()

if __name__ == '__main__':
    main()