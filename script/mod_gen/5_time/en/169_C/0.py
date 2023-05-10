def main():
    a, b = map(str, input().split())
    a = int(a)
    b = int(b.replace('.', ''))
    print(a*b//100)

if __name__ == '__main__':
    main()