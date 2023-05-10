def main():
    S = input()
    S = S.replace('vw','x')
    print(S.count('v')+S.count('w'))

if __name__ == '__main__':
    main()