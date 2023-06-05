def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    min_a = min(a)
    max_b = max(b)
    print(max(0, max_b - min_a + 1))

if __name__ == '__main__':
    main()