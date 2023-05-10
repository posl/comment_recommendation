def main():
    A, B, Q = map(int, input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]
    for i in range(Q):
        l = 0
        r = 0
        while l < A and s[l] < x[i]:
            l += 1
        while r < B and t[r] < x[i]:
            r += 1
        if l == A and r == B:
            print(min(abs(s[-1] - x[i]), abs(t[-1] - x[i])))
        elif l == A:
            print(min(abs(s[-1] - x[i]), abs(t[r] - x[i]), abs(t[r] - x[i]) + abs(t[r] - s[-1])))
        elif r == B:
            print(min(abs(t[-1] - x[i]), abs(s[l] - x[i]), abs(s[l] - x[i]) + abs(s[l] - t[-1])))
        else:
            print(min(abs(s[l] - x[i]), abs(t[r] - x[i]), abs(s[l] - x[i]) + abs(s[l] - t[r]), abs(t[r] - x[i]) + abs(s[l] - t[r])))

if __name__ == '__main__':
    main()