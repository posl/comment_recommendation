def main():
    n = int(input())
    if n%111 == 0:
        print(n)
    else:
        print(n//111*111+111)

if __name__ == '__main__':
    main()