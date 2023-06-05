def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in x:
        print(n - (a.index(i) if i in a else len(a) - 1 - a[::-1].index(i) + 1))

if __name__ == '__main__':
    main()