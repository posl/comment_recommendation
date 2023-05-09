def main():
    # read input
    x, a = map(int, input().split())
    # output
    if x < a:
        print(0)
    else:
        print(10)

if __name__ == '__main__':
    main()