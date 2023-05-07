def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_a = max(A)
    min_a = min(A)
    print(max_a - min_a)

if __name__ == '__main__':
    main()