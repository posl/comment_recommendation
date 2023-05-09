def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print("Yes" if len(set(b) & set(sorted(a, reverse=True)[:k])) > 0 else "No")

if __name__ == '__main__':
    main()