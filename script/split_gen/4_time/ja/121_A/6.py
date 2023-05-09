def main():
    h,w = map(int, input().split())
    h2,w2 = map(int, input().split())
    print((h - h2) * (w - w2))
main()
