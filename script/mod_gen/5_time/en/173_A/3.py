def main():
    N = int(input())
    print(1000 - N%1000 if N%1000 != 0 else 0)

if __name__ == '__main__':
    main()