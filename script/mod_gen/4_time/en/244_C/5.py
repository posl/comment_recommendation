def main():
    N = int(input())
    A = [0] * (2 * N + 1)
    for i in range(1, 2 * N + 1):
        print(i)
        A[i] = 1
        a = int(input())
        if a == 0:
            return
        A[a] = 1
main()

if __name__ == '__main__':
    main()