def main():
    a, b, c = [int(x) for x in input().strip().split()]
    print((a*(a+1) + b*(b+1) + c*(c+1))/2)

if __name__ == '__main__':
    main()