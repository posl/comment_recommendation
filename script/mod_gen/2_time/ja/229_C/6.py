def main():
    n, w = map(int, input().split())
    a = [0]*n
    b = [0]*n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    print(solve(n, w, a, b))

if __name__ == '__main__':
    main()