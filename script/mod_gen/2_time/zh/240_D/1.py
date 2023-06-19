def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = []
    for i in range(n):
        b.append(a[i])
        while len(b) >= 2 and b[-1] == b[-2]:
            b.pop()
            b.pop()
    print(len(b))

if __name__ == '__main__':
    main()