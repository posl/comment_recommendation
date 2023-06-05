def main():
    L, Q = map(int, input().split())
    x = [0, L]
    for i in range(Q):
        c, q = map(int, input().split())
        if c == 1:
            x.append(q)
        else:
            x.sort()
            for j in range(len(x)):
                if x[j] == q:
                    print(x[j+1] - x[j-1])
                    break

if __name__ == '__main__':
    main()