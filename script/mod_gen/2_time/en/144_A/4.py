def main():
    a, b = map(int, input().split())
    if (a >= 1 and a <= 20) and (b >= 1 and b <= 20):
        if a * b <= 20:
            print(a * b)
        else:
            print(-1)
    else:
        print(-1)

if __name__ == '__main__':
    main()