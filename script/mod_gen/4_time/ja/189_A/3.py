def main():
    c1, c2, c3 = input().rstrip().split()
    if c1 == c2 and c2 == c3:
        print('Won')
    else:
        print('Lost')

if __name__ == '__main__':
    main()