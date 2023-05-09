def main():
    n, k = map(int, input().split())
    print( (n*100 + k*10)*n + k*10 )

if __name__ == '__main__':
    main()