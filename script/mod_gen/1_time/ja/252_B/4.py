def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print('Yes' if max(a) in a and max(a) not in b else 'No')

if __name__ == '__main__':
    main()