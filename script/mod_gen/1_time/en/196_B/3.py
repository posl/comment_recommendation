def main():
    x = input()
    if x.find('.') != -1:
        print(x[0:x.find('.')])
    else:
        print(x)

if __name__ == '__main__':
    main()