def main():
    h, w = map(int, input().split())
    hh, ww = map(int, input().split())
    print((h - hh) * (w - ww))

if __name__ == '__main__':
    main()