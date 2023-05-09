def main():
    n = int(input())
    a = []
    b = []
    for i in range(n-1):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    print('Yes' if len(set(a)) == 1 or len(set(b)) == 1 else 'No')

if __name__ == '__main__':
    main()