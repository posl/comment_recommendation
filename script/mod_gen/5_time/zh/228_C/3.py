def main():
    n, k = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(n)]
    p = sorted(p, key=lambda x: (x[0] + x[1] + x[2], x[0], x[1], x[2]), reverse=True)
    for i in range(n):
        if i < k:
            print("Yes")
        else:
            print("No")
    return

if __name__ == '__main__':
    main()