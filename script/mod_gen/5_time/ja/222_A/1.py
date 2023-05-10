def main():
    n = int(input())
    n = str(n)
    while len(n) < 4:
        n = "0" + n
    print(n)

if __name__ == '__main__':
    main()