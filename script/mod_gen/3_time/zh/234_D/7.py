def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    if k == 1:
        print(min(p))
        return
    if k == n:
        print(max(p))
        return
    for i in range(n - k + 1):
        print(max(p[i:i + k]))

if __name__ == '__main__':
    main()