def main():
    x = input()
    x = x.split('.')
    if x[1] == '0':
        print(x[0] + '-')
    elif x[1] == '1' or x[1] == '2':
        print(x[0] + '-')
    elif x[1] == '3' or x[1] == '4' or x[1] == '5' or x[1] == '6':
        print(x[0])
    elif x[1] == '7' or x[1] == '8' or x[1] == '9':
        print(x[0] + '+')

if __name__ == '__main__':
    main()