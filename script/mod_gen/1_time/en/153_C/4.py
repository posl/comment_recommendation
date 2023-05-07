def main():
    n, k = map(int, input().split())
    h = sorted(list(map(int, input().split())), reverse=True)
    print(sum(h[k:]))

if __name__ == '__main__':
    main()