def main():
    N = int(input())
    #print(N)
    if N == 1:
        print(0)
    else:
        print(2**(N-1))

if __name__ == '__main__':
    main()