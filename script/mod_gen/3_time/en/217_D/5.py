def main():
    l, q = map(int, input().split())
    cut = [0, l]
    for i in range(q):
        c, x = map(int, input().split())
        if c == 1:
            cut.append(x)
        else:
            cut.sort()
            idx = cut.index(x)
            print(cut[idx + 1] - cut[idx - 1])

if __name__ == '__main__':
    main()