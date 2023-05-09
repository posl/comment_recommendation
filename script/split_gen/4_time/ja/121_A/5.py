def main():
    h, w = map(int, input().split())
    h2, w2 = map(int, input().split())
    print(h*w - (h2*w + w2*h - h2*w2))
    return
