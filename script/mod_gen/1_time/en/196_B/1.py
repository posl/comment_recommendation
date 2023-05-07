def main():
    x = input()
    if '.' in x:
        print(x[:x.index('.')])
    else:
        print(x)

if __name__ == '__main__':
    main()