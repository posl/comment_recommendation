def main():
    k = int(input())
    a, b = map(int, input().split())
    if a % k == 0 or b % k == 0 or (a + k - 1) // k * k <= b:
        print("OK")
    else:
        print("NG")

if __name__ == '__main__':
    main()