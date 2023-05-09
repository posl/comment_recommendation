def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = sum(a) - n
    print(ans)

if __name__ == '__main__':
    main()