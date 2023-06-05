def main():
    str = input()
    if str.count(str[0]) == 3:
        print('Won')
    else:
        print('Lost')

if __name__ == '__main__':
    main()