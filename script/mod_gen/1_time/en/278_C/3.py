def main():
    # Step #1. Input
    n, q = map(int, input().split())
    t = [0] * q
    a = [0] * q
    b = [0] * q
    for i in range(q):
        t[i], a[i], b[i] = map(int, input().split())
    # Step #2. Solve
    # Step #2-1. Initialize
    ans = [0] * q
    follow = [0] * n
    follower = [0] * n
    for i in range(q):
        if t[i] == 1:
            follow[a[i] - 1] += 1
            follower[b[i] - 1] += 1
        elif t[i] == 2:
            if follow[a[i] - 1] > 0:
                follow[a[i] - 1] -= 1
            if follower[b[i] - 1] > 0:
                follower[b[i] - 1] -= 1
        else:
            if follow[a[i] - 1] > 0 and follower[b[i] - 1] > 0:
                ans[i] = 1
    # Step #2-2. Output
    for i in range(q):
        if ans[i] == 1:
            print('Yes')
        elif t[i] == 3:
            print('No')

if __name__ == '__main__':
    main()