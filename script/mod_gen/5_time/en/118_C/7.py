def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(gcd_list(a))

if __name__ == '__main__':
    main()