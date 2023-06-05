def main():
    a,b = map(int, input().split())
    if a >= b:
        print(2*a+100-b)
    else:
        print(2*a+100)

if __name__ == '__main__':
    main()