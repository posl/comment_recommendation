def main():
    L, Q = map(int, input().split())
    d = [0, L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            d.append(x)
        else:
            d.sort()
            for j in range(len(d)):
                if d[j] == x:
                    print(d[j + 1] - d[j])
                    break

if __name__ == '__main__':
    main()