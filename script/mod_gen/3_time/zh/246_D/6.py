def main():
    n = int(input())
    if n >= 2:
        for i in range(n, 10**18):
            if i == (i**3 + i**2 + i + 1)**(1/3):
                print(i)
                break
    else:
        print(n)

if __name__ == '__main__':
    main()