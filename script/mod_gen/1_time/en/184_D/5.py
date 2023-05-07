def main():
    a,b,c = map(int, input().split())
    print((a*(100-a)/a) + (b*(100-b)/b) + (c*(100-c)/c))

if __name__ == '__main__':
    main()