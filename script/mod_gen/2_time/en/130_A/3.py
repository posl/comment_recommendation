def main():
    x, a = [int(x) for x in input().split()]
    if x < a:
        print(0)
    else:
        print(10)

if __name__ == '__main__':
    main()