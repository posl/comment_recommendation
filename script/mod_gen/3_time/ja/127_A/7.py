def main():
    #input
    a, b = map(int, input().split())
    #output
    if a >= 13:
        print(b)
    elif a >= 6 and a <= 12:
        print(b//2)
    else:
        print(0)

if __name__ == '__main__':
    main()