def main():
    A, B, C, D = map(int, input().split())
    if D*C - B <= 0:
        print(-1)
    else:
        print((A + (D*C - B) - 1) // (D*C - B))

if __name__ == '__main__':
    main()