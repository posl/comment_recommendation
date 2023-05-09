def main():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(0)
    a.insert(0, 0)
    for i in range(1, n + 1):
        for j in range(i + 1, n + 2):
            if a[i] + a[j] <= x and abs(i - j) == a[i] + a[j]:
                print('Yes')
                return
            elif a[i] + a[j] <= y and abs(i - j) == a[i] + a[j]:
                print('Yes')
                return
    print('No')
    return
