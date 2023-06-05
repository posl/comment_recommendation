def main():
    n = input()
    for i in range(len(n)):
        if n[i] == '1':
            print('9', end='')
        elif n[i] == '9':
            print('1', end='')
        else:
            print(n[i], end='')

if __name__ == '__main__':
    main()