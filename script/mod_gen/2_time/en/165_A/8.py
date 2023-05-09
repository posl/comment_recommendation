def main():
    k = int(input())
    a, b = map(int, input().split())
    print("OK" if (b // k - (a - 1) // k) > 0 else "NG")

if __name__ == '__main__':
    main()