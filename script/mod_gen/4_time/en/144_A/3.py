def main():
    a, b = map(int, input().split())
    if (1 <= a <= 20) and (1 <= b <= 20):
        print(a*b)
    else:
        print(-1)

if __name__ == '__main__':
    main()