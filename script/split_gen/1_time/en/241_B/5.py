def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    for i in range(m):
        if a[i] < b[i]:
            print('No')
            return
    print('Yes')
