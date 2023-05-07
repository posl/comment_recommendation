def main():
    a,b = map(int, input().split())
    if a < 1 or a > 20 or b < 1 or b > 20:
        return
    print(a*b)
    return

if __name__ == '__main__':
    main()