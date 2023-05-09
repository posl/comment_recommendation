def main():
    # input
    a, b = map(int, input().split())
    # compute
    ans = max(a+a-1, a+b, b+b-1)
    # output
    print(ans)

if __name__ == '__main__':
    main()