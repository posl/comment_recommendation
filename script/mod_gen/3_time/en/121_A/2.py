def main():
    h, w = map(int, input().split())
    h_p, w_p = map(int, input().split())
    print((h - h_p) * (w - w_p))
main()
