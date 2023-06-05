def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a = a[::-1]
    print(sum(a[:k]))

if __name__ == '__main__':
    main()