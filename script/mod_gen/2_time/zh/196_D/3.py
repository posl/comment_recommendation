def main():
    H, W, A, B = map(int, input().split())
    print(H, W, A, B)
    print(calc(H, W, A, B))

if __name__ == '__main__':
    main()