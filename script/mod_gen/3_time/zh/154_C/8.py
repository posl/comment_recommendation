def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = set(a)
    if len(a) == len(b):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()