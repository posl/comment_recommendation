def main():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    max_b = max(b)
    idx = b.index(max_b)
    print(a[idx] + b[idx])

if __name__ == '__main__':
    main()