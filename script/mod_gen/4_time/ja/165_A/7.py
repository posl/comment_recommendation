def main():
    k = int(input())
    a, b = map(int, input().split())
    if a <= b and a % k == 0:
        print("OK")
    else:
        print("NG")

if __name__ == '__main__':
    main()