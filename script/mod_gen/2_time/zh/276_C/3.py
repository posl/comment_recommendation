def main():
    n = int(input())
    p = list(map(int, input().split()))
    p = [0] + p
    q = [0] * (n + 1)
    for i in range(1, n + 1):
        q[p[i]] = i
    print(' '.join(map(str, q[1:])))

if __name__ == '__main__':
    main()