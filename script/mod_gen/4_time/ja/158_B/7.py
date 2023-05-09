def main():
    n, a, b = map(int, input().split())
    if a == 0:
        print(0)
    elif n <= a+b:
        print(min(a, n))
    else:
        print(min(a, n-a-b))

if __name__ == '__main__':
    main()