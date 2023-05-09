def main():
    alpha = input()
    if alpha.isupper():
        print('A')
    elif alpha.islower():
        print('a')
    else:
        print('Error')
        exit()

if __name__ == '__main__':
    main()