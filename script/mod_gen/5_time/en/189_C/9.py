def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_a = max(a)
    max_index = a.index(max_a)
    a.pop(max_index)
    print(max_a * (n - 1) + sum(a))

if __name__ == '__main__':
    main()