def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    a_list.sort()
    for a in a_list:
        n -= a
        if n < 0:
            print(-1)
            return
    print(n)

if __name__ == '__main__':
    main()