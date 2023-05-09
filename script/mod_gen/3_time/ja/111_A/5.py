def main():
    n = int(input())
    print(str(n)[::-1].replace('1', '2').replace('9', '1').replace('2', '9'))

if __name__ == '__main__':
    main()