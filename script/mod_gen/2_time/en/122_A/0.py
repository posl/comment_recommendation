def main():
    b = input()
    if b == 'A':
        print('T')
    elif b == 'C':
        print('G')
    elif b == 'G':
        print('C')
    elif b == 'T':
        print('A')
    else:
        print('Error: Invalid input')

if __name__ == '__main__':
    main()