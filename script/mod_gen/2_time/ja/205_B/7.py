def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n == len(set(a)):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()