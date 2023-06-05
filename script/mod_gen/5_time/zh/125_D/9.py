def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_abs = list(map(abs, a))
    a_sum = sum(a_abs)
    a_abs_min = min(a_abs)
    if a_abs_min in a:
        if a_sum % 2 == 0:
            print(a_sum)
        else:
            print(a_sum - a_abs_min * 2)
    else:
        print(a_sum)

if __name__ == '__main__':
    main()