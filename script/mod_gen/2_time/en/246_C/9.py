def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(sum([min(x, i) for i in a]) - k * x)

if __name__ == '__main__':
    main()