def main():
    # input
    k = int(input())
    a, b = map(int, input().split())
    # output
    if a % k == 0 or b % k == 0:
        print("OK")
    elif a // k != b // k:
        print("OK")
    else:
        print("NG")

if __name__ == '__main__':
    main()