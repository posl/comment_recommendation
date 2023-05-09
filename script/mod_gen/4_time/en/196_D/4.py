def main():
    H, W, A, B = map(int, input().split())
    print((H - B) * (W - A) * (H - B - 1) * (W - A - 1) // 4)

if __name__ == '__main__':
    main()