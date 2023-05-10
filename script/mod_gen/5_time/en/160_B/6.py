def main():
    x = int(input())
    a = int(x/500)
    x = x - (a*500)
    b = int(x/5)
    print(a*1000 + b*5)

if __name__ == '__main__':
    main()