def main():
    # put your code here
    a, b, c = map(int, input().split())
    print(max(0, c - (a - b)))

if __name__ == '__main__':
    main()