def main():
    n = int(input())
    a = [i for i in range(1, 2*n+2)]
    for i in range(n):
        print(a.pop(0))
        b = int(input())
        if b == 0:
            return
        a.remove(b)
    print(a.pop(0))

if __name__ == '__main__':
    main()