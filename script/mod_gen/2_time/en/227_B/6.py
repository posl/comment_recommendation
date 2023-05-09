def main():
    n = int(input())
    s = list(map(int, input().split()))
    if 4*min(s) < sum(s):
        print(0)
    else:
        print(4*min(s) - sum(s))

if __name__ == '__main__':
    main()