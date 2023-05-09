def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    d = {}
    for i in range(N):
        a = A[i]
        m = a % mod
        if m in d:
            d[m].append(i)
        else:
            d[m] = [i]
    for k, v in d.items():
        if len(v) > 1:
            print('Yes')
            print(len(v), ' '.join([str(i+1) for i in v]))
            print(1, v[0]+1)
            return
    for k, v in d.items():
        for k2, v2 in d.items():
            if k == k2:
                continue
            if (k + k2) % mod == 0:
                print('Yes')
                print(len(v), ' '.join([str(i+1) for i in v]))
                print(len(v2), ' '.join([str(i+1) for i in v2]))
                return
    print('No')
    return

if __name__ == '__main__':
    main()