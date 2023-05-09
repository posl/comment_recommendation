def main():
    A, B = [x for x in input().split()]
    A = int(A)
    B = int(B.replace('.',''))
    print(A*B//100)

if __name__ == '__main__':
    main()