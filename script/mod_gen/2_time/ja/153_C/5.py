def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort(reverse=True)
    ans = sum(h[k:])
    print(ans)

if __name__ == '__main__':
    main()