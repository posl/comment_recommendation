def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    t.reverse()
    a = 0
    b = 0
    for i in range(n):
        if a < b:
            a += t[i]
        else:
            b += t[i]
    print(max(a, b))

if __name__ == '__main__':
    main()