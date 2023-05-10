def main():
    n = int(raw_input().strip())
    sx, sy, tx, ty = map(int, raw_input().strip().split())
    circles = [map(int, raw_input().strip().split()) for _ in xrange(n)]
    print 'Yes' if solve(n, sx, sy, tx, ty, circles) else 'No'

if __name__ == '__main__':
    main()