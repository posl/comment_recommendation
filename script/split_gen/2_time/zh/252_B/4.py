def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(n):
        for j in range(k):
            if i == b[j] - 1:
                a[i] = 0
    if max(a) == 0:
        print('No')
    else:
        print('Yes')
main()
