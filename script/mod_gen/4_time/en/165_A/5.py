def main():
    k = int(input())
    a,b = map(int,input().split())
    if a % k == 0:
        print("OK")
    elif a // k != b // k:
        print("OK")
    else:
        print("NG")

if __name__ == '__main__':
    main()