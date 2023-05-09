def main():
    H, A = map(int, input().split())
    print(H // A + (H % A != 0))

if __name__ == '__main__':
    main()