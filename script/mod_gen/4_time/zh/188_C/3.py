def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(a.index(min(a[:2**(n-1)])) + 1)

if __name__ == '__main__':
    main()