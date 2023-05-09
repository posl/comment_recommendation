def main():
    a, b = map(int, input().split())
    print((b-a)*(b+a-1)//2 - a)

if __name__ == '__main__':
    main()