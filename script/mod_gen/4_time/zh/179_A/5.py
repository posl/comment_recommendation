def main():
    word = input()
    if word[-1] == 's':
        print(word + 'es')
    else:
        print(word + 's')

if __name__ == '__main__':
    main()