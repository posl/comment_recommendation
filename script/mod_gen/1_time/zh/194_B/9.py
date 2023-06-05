def main():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    a = []
    b = []
    for i in range(n):
        a.append(ab[i][0])
        b.append(ab[i][1])
    if max(a) > max(b):
        print(max(a))
    else:
        print(max(b))

if __name__ == '__main__':
    main()