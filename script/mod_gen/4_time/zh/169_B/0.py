def main():
    N = int(input())
    A = list(map(int, input().split()))
    if 0 in A:
        print(0)
        return
    result = 1
    for a in A:
        result *= a
        if result > 10**18:
            print(-1)
            return
    print(result)

if __name__ == '__main__':
    main()