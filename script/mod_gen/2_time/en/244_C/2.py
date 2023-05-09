def main():
    N = int(input())
    a = [0] * (2 * N + 1)
    for i in range(1, 2 * N + 2):
        print(i)
        x = int(input())
        if x == 0:
            return
        a[x] = 1
        if i == 2 * N + 1:
            return
        for j in range(2 * N, 0, -1):
            if a[j] == 0:
                print(j)
                y = int(input())
                if y == 0:
                    return
                a[y] = 1
                break
main()

if __name__ == '__main__':
    main()