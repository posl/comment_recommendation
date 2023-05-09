def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    a_sum = sum(a_list)
    if n >= a_sum:
        print(n - a_sum)
    else:
        print(-1)

if __name__ == '__main__':
    main()