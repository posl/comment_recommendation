def main():
    N, M = map(int, input().split())
    py = [list(map(int, input().split())) for _ in range(M)]
    py.sort()
    city = [0] * N
    for i, (p, y) in enumerate(py):
        city[p - 1] += 1
        py[i].append(city[p - 1])
    for p, y, c in py:
        print(str(p).zfill(6) + str(c).zfill(6))

if __name__ == '__main__':
    main()