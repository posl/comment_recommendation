def main():
    n = input()
    if n.find('.') != -1:
        n = n[:n.find('.')]
    print(n)

if __name__ == '__main__':
    main()