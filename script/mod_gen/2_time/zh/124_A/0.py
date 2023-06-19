def main():
    a,b = map(int, input().split())
    print(max(a+a-1, a+b, b+b-1))

if __name__ == '__main__':
    main()