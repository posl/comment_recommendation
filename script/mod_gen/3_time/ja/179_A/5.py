def main():
    #input
    S = input()
    #output
    if S[-1] == 's':
        print(S + 'es')
    else:
        print(S + 's')

if __name__ == '__main__':
    main()