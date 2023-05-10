def main():
    n = input()
    print(n.translate(str.maketrans('19', '91')))

if __name__ == '__main__':
    main()