def main():
    k = int(input())
    a, b = map(str, input().split())
    a = int(a, k)
    b = int(b, k)
    print(a*b)

if __name__ == '__main__':
    main()