def main():
    N = int(input())
    if N == 1:
        print(0)
        return
    print(2**(N-1)-1)

if __name__ == '__main__':
    main()