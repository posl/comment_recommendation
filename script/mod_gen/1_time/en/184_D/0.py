def main():
    a, b, c = map(int, input().split())
    print((a*(a+1) / (a+b+c)) + (b*(b+1) / (a+b+c)) + (c*(c+1) / (a+b+c)))

if __name__ == '__main__':
    main()