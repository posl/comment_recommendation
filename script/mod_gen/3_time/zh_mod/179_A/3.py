def main():
    S = input()
    if S.endswith('s'):
        print(S + 'es')
    else:
        print(S + 's')

if __name__ == '__main__':
    main()