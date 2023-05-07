def main():
    N = int(input())
    A = list(map(int, input().split()))
    c2 = 0
    c3 = 0
    for a in A:
        while a % 2 == 0:
            c2 += 1
            a //= 2
        while a % 3 == 0:
            c3 += 1
            a //= 3
        if a != 1:
            print(-1)
            return
    print(c2 + c3)

if __name__ == '__main__':
    main()