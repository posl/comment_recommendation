def main():
    N = int(input())
    i = 1
    while i*(i+1) < N:
        i += 1
    print(i-1+i)

if __name__ == '__main__':
    main()