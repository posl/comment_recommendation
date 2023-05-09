def main():
    #input
    n, a, b = map(int, input().split())
    #output
    print(min(n*a, b))

if __name__ == '__main__':
    main()