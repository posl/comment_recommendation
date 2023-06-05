def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n % 2 == 0:
        i = 0
        j = n - 1
        while i < j:
            if a[i] != a[i + 1] or a[j] != a[j - 1]:
                print(0)
                return
            i += 2
            j -= 2
        print(2 ** (n // 2) % (10 ** 9 + 7))
    else:
        i = 1
        j = n - 1
        while i < j:
            if a[i] != a[i + 1] or a[j] != a[j - 1]:
                print(0)
                return
            i += 2
            j -= 2
        print(2 ** (n // 2) % (10 ** 9 + 7))
