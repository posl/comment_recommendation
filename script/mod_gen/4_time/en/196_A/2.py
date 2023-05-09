def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(a-c, b-d))

if __name__ == '__main__':
    main()