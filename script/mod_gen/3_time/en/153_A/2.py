def main():
    #input
    H, A = map(int, input().split())
    #output
    print((H + A - 1) // A)

if __name__ == '__main__':
    main()