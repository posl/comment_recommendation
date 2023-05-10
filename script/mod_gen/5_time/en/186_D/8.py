def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    s = 0
    for i in range(N):
        s += (A[i] - A[0]) * (2 * i - N + 1)
    print(s)

if __name__ == '__main__':
    main()