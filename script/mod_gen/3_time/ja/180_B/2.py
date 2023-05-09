def main():
    n = int(input())
    x = list(map(int, input().split()))
    x = list(map(abs, x))
    print(sum(x))
    print(sum([i**2 for i in x])**0.5)
    print(max(x))

if __name__ == '__main__':
    main()