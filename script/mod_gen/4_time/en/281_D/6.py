def main():
    n, k, d = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    if n < k:
        print(-1)
        return
    if k == 1:
        print(a[0] % d)
        return
    if k == 2:
        for i in range(n-1):
            if a[i] % d == 0:
                print(a[i] % d)
                return
            if (a[i] + a[i+1]) % d == 0:
                print(a[i] + a[i+1])
                return
        print(-1)
        return
    if k == 3:
        for i in range(n-2):
            if a[i] % d == 0:
                print(a[i] % d)
                return
            for j in range(i+1, n-1):
                if (a[i] + a[j]) % d == 0:
                    print(a[i] + a[j])
                    return
                for k in range(j+1, n):
                    if (a[i] + a[j] + a[k]) % d == 0:
                        print(a[i] + a[j] + a[k])
                        return
        print(-1)
        return
    if k == 4:
        for i in range(n-3):
            if a[i] % d == 0:
                print(a[i] % d)
                return
            for j in range(i+1, n-2):
                if (a[i] + a[j]) % d == 0:
                    print(a[i] + a[j])
                    return
                for k in range(j+1, n-1):
                    if (a[i] + a[j] + a[k]) % d == 0:
                        print(a[i] + a[j] + a[k])
                        return
                    for l in range(k+1, n):
                        if (a[i] + a[j] + a[k] + a[l]) % d == 0:
                            print(a[i] + a[j] + a[k] + a[l])
                            return
        print(-1)
        return

if __name__ == '__main__':
    main()