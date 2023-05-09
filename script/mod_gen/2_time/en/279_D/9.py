def main():
    a,b = map(int, input().split())
    print(a**0.5 + (a-1)/b)

if __name__ == '__main__':
    main()