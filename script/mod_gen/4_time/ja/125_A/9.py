def main():
    a, b, t = map(int, input().split())
    print(int(b * (t // a)))

if __name__ == '__main__':
    main()