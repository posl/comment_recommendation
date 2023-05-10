def inputs():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    return h, w, s

if __name__ == '__main__':
    inputs()