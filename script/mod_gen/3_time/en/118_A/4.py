def main():
    #Read input from console
    a, b = [int(x) for x in input().split()]
    if b % a == 0:
        print(a + b)
    else:
        print(b - a)

if __name__ == '__main__':
    main()