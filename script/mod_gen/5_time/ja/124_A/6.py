def main():
    a, b = map(int, input().split())
    if a >= b:
        print(a*2-1)
    else:
        print(b*2-1)

if __name__ == '__main__':
    main()