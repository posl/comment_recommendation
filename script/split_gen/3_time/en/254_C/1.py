def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if n == k:
        if len(set(a)) == 1:
            print('Yes')
        else:
            print('No')
        return
    if len(set(a)) == 1:
        print('Yes')
        return
    if k % 2 == 0:
        for i in range(n - k):
            if a[i] == a[i + k]:
                print('Yes')
                return
        print('No')
        return
    for i in range(n - k):
        if a[i] == a[i + k]:
            print('Yes')
            return
    print('No')
    return
