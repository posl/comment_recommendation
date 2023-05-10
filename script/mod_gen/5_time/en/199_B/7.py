def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    min_a = max(a)
    max_b = min(b)
    if min_a > max_b:
        print(0)
    else:
        print(max_b - min_a + 1)

if __name__ == '__main__':
    main()