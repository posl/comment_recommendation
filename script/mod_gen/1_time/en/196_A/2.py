def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(b-d, a-c))

if __name__ == '__main__':
    main()