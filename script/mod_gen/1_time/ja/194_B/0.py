def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a_min = min(a)
    b_min = min(b)
    a_min_index = a.index(a_min)
    b_min_index = b.index(b_min)
    if a_min_index == b_min_index:
        a.remove(a_min)
        b.remove(b_min)
        a_second_min = min(a)
        b_second_min = min(b)
        print(min(a_min + b_second_min, a_second_min + b_min))
    else:
        print(max(a_min, b_min))

if __name__ == '__main__':
    main()