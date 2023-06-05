def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    # 1. m mod a_1 + m mod a_2 + ... + m mod a_N = m mod (a_1 * a_2 * ... * a_N)
    # 2. 1 <= m mod (a_1 * a_2 * ... * a_N) < a_1 * a_2 * ... * a_N
    # 3. m mod (a_1 * a_2 * ... * a_N) = a_1 * a_2 * ... * a_N - 1
    # 4. m = k * (a_1 * a_2 * ... * a_N) + (a_1 * a_2 * ... * a_N - 1)
    # 5. f(m) = f(a_1 * a_2 * ... * a_N - 1) = a_1 * a_2 * ... * a_N * N - N
    # 6. f(m) = a_1 * a_2 * ... * a_N * N - N
    # 7. f(m) = a_1 * a_2 * ... * a_N * (N - 1)
    # 8. f(m) = a_1 * a_2 * ... * a_N * (N - 1) < a_1 * a_2 * ... * a_N * N
    # 9. f(m) < a_1 * a_2 * ... * a_N * N
    # 10. f(m) < a_1 * a_2 * ... * a_N * N = a_1 * a_2 * ... * a_N * (N - 1) = f(m)
    # 11. f(m) < f(m)
    # 12. f(m) = f(m)
    print(a[0] * a[1] * ... * a[N-1] * (N - 1))

if __name__ == '__main__':
    main()