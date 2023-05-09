def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a_max = max(a)
    a_min = min(a)
    a_max_count = a.count(a_max)
    a_min_count = a.count(a_min)
    if a_max == a_min:
        for _ in range(n):
            print(a_max)
    else:
        for i in range(n):
            if a[i] == a_max:
                if a_max_count == 1:
                    print(a_min)
                else:
                    print(a_max)
            else:
                print(a_max)

if __name__ == '__main__':
    main()