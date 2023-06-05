def main():
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0)
        return
    p = 1
    for i in a:
        p *= i
        if p > 10**18:
            print(-1)
            return
    print(p)
    return

if __name__ == '__main__':
    main()