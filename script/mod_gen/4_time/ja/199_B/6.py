def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    max_a = max(a)
    min_b = min(b)
    if min_b >= max_a:
        print(min_b - max_a + 1)
    else:
        print(0)

if __name__ == '__main__':
    main()