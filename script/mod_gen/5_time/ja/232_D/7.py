def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    print(H, W, C)
    print(C[0][0])
    print(C[0][1])
    print(C[1][0])
    print(C[1][1])

if __name__ == '__main__':
    main()