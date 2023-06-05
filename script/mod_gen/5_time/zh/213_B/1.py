def main():
    n = int(input())
    a = list(map(int,input().split()))
    second = min(a)
    a.remove(second)
    print(a.index(min(a))+2)

if __name__ == '__main__':
    main()