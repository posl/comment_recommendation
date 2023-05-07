def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_max = 0
    a_sum = 0
    for a in a_list:
        a_sum += a
        a_max = max(a_max, a_sum)
    print(a_max)

if __name__ == '__main__':
    main()