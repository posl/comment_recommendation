def main():
    n = int(input())
    v = list(map(int, input().split()))
    a = v[::2]
    b = v[1::2]
    from collections import Counter
    a_c = Counter(a).most_common()
    b_c = Counter(b).most_common()
    if a_c[0][0] != b_c[0][0]:
        print(n - a_c[0][1] - b_c[0][1])
    else:
        if len(a_c) == 1 and len(b_c) == 1:
            print(n // 2)
        elif len(a_c) == 1:
            print(n - b_c[1][1])
        elif len(b_c) == 1:
            print(n - a_c[1][1])
        else:
            print(n - max(a_c[0][1] + b_c[1][1], a_c[1][1] + b_c[0][1]))

if __name__ == '__main__':
    main()