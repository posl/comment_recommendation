def main():
    a, b = map(int, input().split())
    a_sum = 0
    b_sum = 0
    for i in range(3):
        a_sum += a % 10
        a //= 10
        b_sum += b % 10
        b //= 10
    if a_sum > b_sum:
        print(a_sum)
    else:
        print(b_sum)

if __name__ == '__main__':
    main()