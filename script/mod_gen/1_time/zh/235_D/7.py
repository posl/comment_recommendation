def main():
    a,n = map(int,input().split())
    if a%2 == 0 and n%2 == 1:
        print(-1)
        return
    if a%5 == 0 and n%5 == 1:
        print(-1)
        return
    if a%5 == 1 and n%5 == 0:
        print(-1)
        return
    if a%2 == 1 and a%5 == 1:
        print(-1)
        return
    if a%2 == 1 and a%5 == 4:
        print(-1)
        return
    if a%2 == 1 and a%5 == 2:
        print(-1)
        return
    if a%2 == 1 and a%5 == 3:
        print(-1)
        return
    if a%2 == 0 and a%5 == 2:
        print(-1)
        return
    if a%2 == 0 and a%5 == 3:
        print(-1)
        return
    if a%2 == 0 and a%5 == 4:
        print(-1)
        return
    if a%2 == 0 and a%5 == 0:
        print(-1)
        return
    if a%2 == 0 and a%5 == 1:
        print(-1)
        return
    if a%2 == 1 and a%5 == 0:
        print(-1)
        return
    if a%2 == 1 and a%5 == 1:
        print(-1)
        return
    if a%2 == 1 and a%5 == 4:
        print(-1)
        return
    if a%2 == 1 and a%5 == 3:
        print(-1)
        return
    if a%2 == 1 and a%5 == 2:
        print(-1)
        return
    if a%2 == 0 and a%5 == 2:
        print(-1)
        return
    if a%2 == 0 and a%5 == 3:
        print(-1)
        return
    if a%2 == 0 and a%5 == 4:
        print(-1)
        return
    if a%2 == 0

if __name__ == '__main__':
    main()