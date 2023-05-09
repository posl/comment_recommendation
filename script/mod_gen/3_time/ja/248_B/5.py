def main():
    a, b, k = map(int, input().split())
    if a >= b:
        print(0)
        return
    for i in range(k):
        if a * 2 < b:
            a *= 2
        else:
            a += b
            print(a - b)
            return
    print(a - b)

if __name__ == '__main__':
    main()