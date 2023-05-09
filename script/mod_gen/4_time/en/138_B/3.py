def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_sum = 0
    for a in a_list:
        a_sum += 1/a
    print(1/a_sum)

if __name__ == '__main__':
    main()