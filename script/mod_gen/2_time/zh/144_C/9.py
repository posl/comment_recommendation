def main():
    n = int(input())
    i = 1
    while i*i <= n:
        i += 1
    print(i-1)

if __name__ == '__main__':
    main()