def problems121_a():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print(H * W - (h * W + w * H - h * w))

if __name__ == '__main__':
    problems121_a()