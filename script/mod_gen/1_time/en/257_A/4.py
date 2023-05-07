def main():
    N, X = map(int, input().split())
    A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = ''
    for i in range(N):
        s += A
    print(s[X-1])

if __name__ == '__main__':
    main()