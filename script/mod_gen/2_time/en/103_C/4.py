def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = sum(a) - n
    print(ans)

if __name__ == '__main__':
    main()