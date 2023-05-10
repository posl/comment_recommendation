def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    max_a = max(a)
    max_b = max(b)
    min_a = min(a)
    min_b = min(b)
    max_val = max(max_a, max_b)
    min_val = min(min_a, min_b)
    if max_val - min_val > k:
        print("No")
        return
    print("Yes")

if __name__ == '__main__':
    main()