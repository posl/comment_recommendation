def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(sum([min(x, ai) for ai in a]))

if __name__ == '__main__':
    main()