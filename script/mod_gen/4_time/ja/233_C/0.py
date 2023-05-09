def main():
    N, X = map(int, input().split())
    L = []
    A = []
    for i in range(N):
        l, *a = map(int, input().split())
        L.append(l)
        A.append(a)
    cnt = 0
    for i in range(1, 2**N):
        s = []
        for j in range(N):
            if i & (1<<j):
                s.append(A[j])
        if len(s) == 0:
            continue
        r = [1]
        for k in range(len(s)):
            r = [x*y for x in r for y in s[k]]
        if sum(r) == X:
            cnt += 1
    print(cnt)
main()

if __name__ == '__main__':
    main()