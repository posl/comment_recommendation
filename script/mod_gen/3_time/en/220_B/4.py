def main():
    k = int(input())
    a, b = map(str, input().split())
    print(int(a, k)*int(b, k))

if __name__ == '__main__':
    main()