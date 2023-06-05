def main():
    x = input()
    if x.find('.') != -1:
        x = x[:x.find('.')]
    print(x)

if __name__ == '__main__':
    main()