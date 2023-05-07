def main():
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    min_a = min(a)
    min_b = min(b)
    if a.index(min_a) != b.index(min_b):
        print(min(min_a, min_b))
    else:
        a.pop(a.index(min_a))
        b.pop(b.index(min_b))
        print(min(min_a+min(b), min_b+min(a)))

if __name__ == '__main__':
    main()