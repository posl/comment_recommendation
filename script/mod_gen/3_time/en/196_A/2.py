def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(b-d, c-a))

if __name__ == '__main__':
    main()