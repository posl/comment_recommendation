def main():
    n = int(input())
    print(1000-(n%1000) if n%1000 else 0)

if __name__ == '__main__':
    main()