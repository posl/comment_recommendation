def main():
    x = input()
    if '.' in x:
        print(x[0:x.find('.')])
    else:
        print(x)
main()

if __name__ == '__main__':
    main()