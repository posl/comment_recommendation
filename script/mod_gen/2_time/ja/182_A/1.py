def main():
    a, b = map(int, input().split())
    if a*2+100 >= b:
        print(a*2+100-b)
    else:
        print(0)

if __name__ == '__main__':
    main()