def main():
    a, b = map(int, input().split())
    x = (b-a-1)*(a+b)//2
    print(x-a)

if __name__ == '__main__':
    main()