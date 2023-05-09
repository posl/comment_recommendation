def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(b-d, a-c, b-c, a-d))

if __name__ == '__main__':
    main()