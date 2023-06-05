def main():
    import sys
    N = int(sys.stdin.readline().strip())
    A = [int(i) for i in sys.stdin.readline().strip().split()]
    d = {}
    for i in A:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    cnt = 0
    for i in d:
        if d[i] > 1:
            cnt += d[i] - 1
    print(cnt)

if __name__ == '__main__':
    main()