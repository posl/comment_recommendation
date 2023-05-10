def problems270_b():
    x, y, z = map(int, input().split())
    if x < y < z:
        print(-1)
    else:
        print(x - z - y)

if __name__ == '__main__':
    problems270_b()