def main():
    L, Q = map(int, input().split())
    cuts = [0, L]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            left = cuts.index(x) - 1
            right = left + 1
            print(cuts[right] - cuts[left])

if __name__ == '__main__':
    main()