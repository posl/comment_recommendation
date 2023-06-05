def main():
    x = input()
    if '.' in x:
        i = x.index('.')
        x = x[:i]
    print(x)

if __name__ == '__main__':
    main()