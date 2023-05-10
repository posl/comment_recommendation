def main():
    n = int(input())
    i = 1
    while i**2 <= n:
        if n % i == 0:
            print(i)
            if i**2 != n:
                print(n//i)
        i += 1

if __name__ == '__main__':
    main()