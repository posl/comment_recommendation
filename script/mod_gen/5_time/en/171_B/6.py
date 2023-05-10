def problems171_b():
    n, k = map(int, input().split())
    p = sorted(list(map(int, input().split())))
    print(sum(p[:k]))

if __name__ == '__main__':
    problems171_b()