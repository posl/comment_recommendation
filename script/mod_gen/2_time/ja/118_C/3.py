def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(gcd_list(A))

if __name__ == '__main__':
    main()