def main():
    n = int(input())
    if n%100 != 0:
        print(n//100+1)
    else:
        print(n//100)

if __name__ == '__main__':
    main()