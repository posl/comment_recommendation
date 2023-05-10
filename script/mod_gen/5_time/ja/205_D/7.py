def problem205d():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    ans = []
    for i in range(q):
        tmp = k[i]
        ans.append(tmp)
        for j in range(n):
            if tmp >= a[j]:
                tmp += 1
        ans[i] = tmp
    for i in range(q):
        print(ans[i])

if __name__ == '__main__':
    problem205d()