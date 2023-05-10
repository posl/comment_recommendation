def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    print(len([x for x in a if x < p]))

if __name__ == '__main__':
    main()