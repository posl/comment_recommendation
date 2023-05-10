def main():
    h1, w1 = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h1)]
    h2, w2 = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(h2)]
    print('Yes' if a.count(b[0]) > 0 else 'No')

if __name__ == '__main__':
    main()