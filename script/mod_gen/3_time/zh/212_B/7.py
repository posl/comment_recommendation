def main():
    pin = input()
    if len(set(pin)) == 1:
        print('Weak')
    elif pin in '0123 1234 2345 3456 4567 5678 6789 7890 8901 9012'.split():
        print('Weak')
    else:
        print('Strong')

if __name__ == '__main__':
    main()