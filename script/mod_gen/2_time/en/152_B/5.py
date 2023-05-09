def main():
    a, b = map(int, input().split())
    if a == b:
        print(str(a) * a)
    else:
        print(str(min(a, b)) * max(a, b))

if __name__ == '__main__':
    main()