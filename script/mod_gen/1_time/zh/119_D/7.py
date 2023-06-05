def main():
    A, B, Q = map(int, input().split())
    s = [0] * (A + 2)
    t = [0] * (B + 2)
    x = [0] * (Q + 2)
    for i in range(1, A + 1):
        s[i] = int(input())
    for i in range(1, B + 1):
        t[i] = int(input())
    for i in range(1, Q + 1):
        x[i] = int(input())
    s[0] = -float('inf')
    s[A + 1] = float('inf')
    t[0] = -float('inf')
    t[B + 1] = float('inf')
    for i in range(1, Q + 1):
        j = 0
        while s[j] < x[i]:
            j += 1
        k = 0
        while t[k] < x[i]:
            k += 1
        print(min(max(x[i] - s[j - 1], t[k] - x[i]) + min(x[i] - s[j - 1], t[k] - x[i]), max(s[j] - x[i], x[i] - t[k - 1]) + min(s[j] - x[i], x[i] - t[k - 1])))

if __name__ == '__main__':
    main()