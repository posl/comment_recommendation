def main():
    l, q = map(int, input().split())
    cuts = [0, l]
    for _ in range(q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        elif c == 2:
            cuts.sort()
            for i in range(len(cuts)):
                if cuts[i] == x:
                    print(cuts[i+1] - cuts[i-1])
                    break

if __name__ == '__main__':
    main()