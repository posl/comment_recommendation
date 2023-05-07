def main():
    X = input()
    if X == X[0]*4 or X in ['0123','1234','2345','3456','4567','5678','6789','7890','8901','9012']:
        print('Weak')
    else:
        print('Strong')

if __name__ == '__main__':
    main()