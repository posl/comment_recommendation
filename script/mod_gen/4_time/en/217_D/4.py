def main():
    L, Q = map(int, input().split())
    Lst = [L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            Lst.append(x)
            Lst.append(L - x)
            Lst.sort()
        else:
            for j in range(len(Lst)):
                if Lst[j] >= x:
                    print(Lst[j])
                    break

if __name__ == '__main__':
    main()