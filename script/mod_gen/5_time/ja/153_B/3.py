def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print("Yes" if h <= sum(a) else "No")

if __name__ == '__main__':
    main()