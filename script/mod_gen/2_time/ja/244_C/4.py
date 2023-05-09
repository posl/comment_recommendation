def main():
    N = int(input())
    a = [0] * (2 * N + 1)
    for i in range(1, 2 * N + 2):
        print(i)
        a[i] = 1
        if i == 2 * N + 1:
            return
        j = int(input())
        if j == 0:
            return
        a[j] = 1
main()

if __name__ == '__main__':
    main()