def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort(reverse=True)
    for i in range(k):
        h[i] = 0
    print(sum(h))

if __name__ == '__main__':
    main()