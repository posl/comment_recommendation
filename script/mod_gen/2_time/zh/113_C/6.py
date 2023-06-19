def main():
    N, M = map(int, input().split())
    PY = [list(map(int, input().split())) for i in range(M)]
    PY.sort(key=lambda x: x[1])
    city = [0] * (N + 1)
    for p, y in PY:
        city[p] += 1
        print("{:06d}{:06d}".format(p, city[p]))

if __name__ == '__main__':
    main()