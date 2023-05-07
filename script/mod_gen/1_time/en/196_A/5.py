def main():
    #input
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    #output
    print(max(b - c, d - a))

if __name__ == '__main__':
    main()