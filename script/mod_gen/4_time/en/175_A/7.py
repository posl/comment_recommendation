def main():
    S = input()
    S = S.replace('S', '0')
    S = S.replace('R', '1')
    print(S.count('0'))

if __name__ == '__main__':
    main()