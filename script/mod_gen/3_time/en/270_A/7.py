def main():
    a,b = map(int, input().split())
    c = a | b
    d = 7 - c
    print(d)

if __name__ == '__main__':
    main()