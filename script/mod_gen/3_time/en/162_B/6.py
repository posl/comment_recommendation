def main():
    n = int(input())
    if n % 3 == 0:
        n3 = n // 3 - 1
    else:
        n3 = n // 3
    if n % 5 == 0:
        n5 = n // 5 - 1
    else:
        n5 = n // 5
    if n % 15 == 0:
        n15 = n // 15 - 1
    else:
        n15 = n // 15
    sum3 = 3 * n3 * (n3 + 1) // 2
    sum5 = 5 * n5 * (n5 + 1) // 2
    sum15 = 15 * n15 * (n15 + 1) // 2
    print(sum3 + sum5 - sum15)
main()

if __name__ == '__main__':
    main()