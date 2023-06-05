def main():
    H, W, A, B = map(int, input().split())
    print(rec(0, 0, A, B, H, W))

if __name__ == '__main__':
    main()