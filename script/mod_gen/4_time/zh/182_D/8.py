def main():
    n = int(raw_input())
    a = map(int, raw_input().split())
    b = [0] * n
    b[0] = a[0]
    for i in range(1, n):
        b[i] = b[i-1] + a[i]
    print max(b)

if __name__ == '__main__':
    main()