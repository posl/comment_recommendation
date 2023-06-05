def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    # x = 1
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) % 200 == 0:
                print('Yes')
                print(1, i+1)
                print(1, j+1)
                return
    # x = 2
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (a[i] + a[j] + a[k]) % 200 == 0:
                    print('Yes')
                    print(2, i+1, j+1)
                    print(1, k+1)
                    return
    # x = 3
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if (a[i] + a[j] + a[k] + a[l]) % 200 == 0:
                        print('Yes')
                        print(3, i+1, j+1, k+1)
                        print(1, l+1)
                        return
    # x = 4
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    for m in range(l+1, n):
                        if (a[i] + a[j] + a[k] + a[l] + a[m]) % 200 == 0:
                            print('Yes')
                            print(4, i+1, j+1, k+1, l+1)
                            print(1, m+1)
                            return
    # x = 5
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    for m in range(l+1, n):
                        for o in range(m+1, n):
                            if (a[i] + a[j] + a[k] + a[l] + a[m] +
