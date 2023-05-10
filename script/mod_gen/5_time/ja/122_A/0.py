def main():
    b = input()
    if b == 'A':
        print('T')
    elif b == 'T':
        print('A')
    elif b == 'C':
        print('G')
    elif b == 'G':
        print('C')
    else:
        print('入力はA,T,C,Gのいずれかでお願いします。')

if __name__ == '__main__':
    main()