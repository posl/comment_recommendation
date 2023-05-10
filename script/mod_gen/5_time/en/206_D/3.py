def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_max = max(a)
    a_min = min(a)
    if a_max == a_min:
        print(0)
        return
    a_max_count = a.count(a_max)
    a_min_count = a.count(a_min)
    if (a_max_count + a_min_count) == n:
        print(1)
        return
    a_max_index = a.index(a_max)
    a_min_index = a.index(a_min)
    if a_max_index < a_min_index:
        if a_max_count > a_min_count:
            print(n - a_max_count)
        else:
            print(n - a_min_count)
    else:
        if a_max_count > a_min_count:
            print(n - a_min_count)
        else:
            print(n - a_max_count)

if __name__ == '__main__':
    main()