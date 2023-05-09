def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    p = 0
    for i in range(n):
        p += 1
        if p == 4:
            p -= 4
    print(p)

if __name__ == '__main__':
    main()