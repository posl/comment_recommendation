def main():
    n = int(input())
    a = [0] * (2 * n + 1)
    for i in range(1, 2 * n + 1):
        print(i)
        a[i] = 1
        j = int(input())
        if j == 0:
            break
        a[j] = 1

if __name__ == '__main__':
    main()