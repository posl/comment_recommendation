def main():
    n = int(input())
    print(n%1000)
    if n%1000 == 0:
        print(0)
    else:
        print(1000-(n%1000))
main()

if __name__ == '__main__':
    main()