def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        a.append(tmp[0])
        b.append(tmp[1])
    print(sum(b) - sum(a) + n)

if __name__ == '__main__':
    main()