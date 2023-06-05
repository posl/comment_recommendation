def main():
    N = int(input())
    print(1+sum([i*((1/N)**i) for i in range(1,N)]))

if __name__ == '__main__':
    main()