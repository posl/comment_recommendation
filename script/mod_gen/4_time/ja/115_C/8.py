def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort()
    print(h[K-1] - h[0])

if __name__ == '__main__':
    main()