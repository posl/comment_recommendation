def main():
    n = int(input())
    n = str(n)
    n = n.replace('1', '2')
    n = n.replace('9', '1')
    n = n.replace('2', '9')
    print(n)

if __name__ == '__main__':
    main()