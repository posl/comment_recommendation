def main():
    a, b = map(int, input().split())
    x = b-a-1
    print(x*(x+1)//2 - a)

if __name__ == '__main__':
    main()