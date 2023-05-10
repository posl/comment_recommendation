def main():
    a, b, c = map(int, input().split())
    print(min(abs(a-b)+abs(b-c), abs(a-c)+abs(b-c), abs(a-b)+abs(a-c)))

if __name__ == '__main__':
    main()