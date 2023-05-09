def main():
    L, Q = map(int, input().split())
    cut = [0, L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cut.append(x)
        else:
            cut.sort()
            for j in range(len(cut)):
                if cut[j] == x:
                    print(cut[j + 1] - cut[j - 1])
                    break

if __name__ == '__main__':
    main()