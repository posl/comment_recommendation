def main():
    k = int(input())
    a, b = map(int, input().split())
    print(int(str(a * b), k))

if __name__ == '__main__':
    main()