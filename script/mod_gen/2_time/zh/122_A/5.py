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
        print('输入的字母不是A、C、G和T中的一个字母。')

if __name__ == '__main__':
    main()