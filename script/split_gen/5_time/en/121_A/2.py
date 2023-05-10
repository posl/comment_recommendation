def main():
    h, w = map(int, input().split())
    hh, ww = map(int, input().split())
    print(h*w - (hh*w + ww*h - hh*ww))
