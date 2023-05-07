def main():
    n = int(input())
    a = list(map(int, input().split()))
    if len(a) != len(set(a)):
        print('NO')
    else:
        print('YES')

if __name__ == '__main__':
    main()