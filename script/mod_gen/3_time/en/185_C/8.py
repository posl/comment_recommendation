def main():
    L = int(input())
    if L == 12:
        print(1)
    else:
        print(2**(L - 12))

if __name__ == '__main__':
    main()