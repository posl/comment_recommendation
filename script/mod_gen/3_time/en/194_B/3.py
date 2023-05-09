def main():
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a_min = min(a)
    a_min_index = a.index(a_min)
    b_min = min(b)
    b_min_index = b.index(b_min)
    if a_min_index != b_min_index:
        print(max(a_min, b_min))
    else:
        a_min_2 = sorted(a)[1]
        b_min_2 = sorted(b)[1]
        print(min(max(a_min, b_min_2), max(a_min_2, b_min)))

if __name__ == '__main__':
    main()